"""
Amazon S3 Client
Uploads raw JSON to S3.
"""

import json
import boto3

from utils.logger import logger
from utils.exceptions import StorageException

from config import (
    AWS_REGION,
    S3_BUCKET
)


class S3Client:

    def __init__(self):

        self.client = boto3.client(
            "s3",
            region_name=AWS_REGION
        )

    def upload_json(self, data, key):

        try:

            # Convert list into JSON Lines (NDJSON)
            if isinstance(data, list):

                body = "\n".join(
                    json.dumps(record)
                    for record in data
                )

            else:

                body = json.dumps(data)

            self.client.put_object(

                Bucket=S3_BUCKET,

                Key=key,

                Body=body,

                ContentType="application/json"

            )

            logger.info(
                f"Uploaded to S3 : {key}"
            )

        except Exception as e:

            raise StorageException(e)

    def upload_json_lines(self, data, key):

        body = "\n".join(
            json.dumps(record)
            for record in data
        )

        self.client.put_object(
            Bucket=S3_BUCKET,
            Key=key,
            Body=body,
            ContentType="application/json"
        )

        logger.info(f"Uploaded JSON Lines : {key}")    

   
        