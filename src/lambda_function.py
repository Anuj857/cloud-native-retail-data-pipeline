"""
AWS Lambda Entry Point
"""

import json
from datetime import datetime

from clients.api_client import APIClient
from clients.s3_client import S3Client
from clients.dynamodb_client import DynamoDBClient

from transforms.product_transform import ProductTransformer

from config import (
    PRODUCT_API,
    RAW_PRODUCTS_PATH
)

from utils.logger import logger
from utils.helpers import generate_s3_filename


def lambda_handler(event, context):

    logger.info("========== Lambda Started ==========")

    api_client = APIClient()

    s3_client = S3Client()

    dynamodb_client = DynamoDBClient()

    # Fetch Product Data
    products = api_client.fetch(PRODUCT_API)

    # Upload Raw JSON
    file_name = generate_s3_filename("products")

    s3_key = f"{RAW_PRODUCTS_PATH}/{file_name}"

    s3_client.upload_json(
        products,
        s3_key
    )

    # Transform
    dataframe = ProductTransformer.transform(products)

    # Upload to DynamoDB
    dynamodb_client.batch_insert(dataframe)

    logger.info("========== Pipeline Completed ==========")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Pipeline Executed Successfully",
                "records_processed": len(dataframe),
                "timestamp": datetime.utcnow().isoformat()
            }
        )
    }