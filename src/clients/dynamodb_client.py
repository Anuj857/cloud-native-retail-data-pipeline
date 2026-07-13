"""
Amazon DynamoDB Client
"""

import boto3

from utils.logger import logger
from utils.exceptions import StorageException

from config import (
    AWS_REGION,
    DYNAMODB_TABLE
)


class DynamoDBClient:

    def __init__(self):

        resource = boto3.resource(
            "dynamodb",
            region_name=AWS_REGION
        )

        self.table = resource.Table(
            DYNAMODB_TABLE
        )

    def batch_insert(
        self,
        dataframe
    ):

        try:

            with self.table.batch_writer() as batch:

                for _, row in dataframe.iterrows():

                    batch.put_item(

                        Item={

                            "product_id": str(row["id"]),

                            "title": row["title"],

                            "price": str(row["price"]),

                            "category": row["category"],

                            "rating_rate": str(
                                row["rating_rate"]
                            ),

                            "rating_count": str(
                                row["rating_count"]
                            )

                        }

                    )

            logger.info(
                "Inserted records into DynamoDB"
            )

        except Exception as e:

            raise StorageException(e)