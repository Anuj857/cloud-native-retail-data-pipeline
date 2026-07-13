"""
Amazon S3 Client
Uploads raw JSON to S3.
"""

import boto3

from utils.logger import logger
from utils.helpers import convert_to_json
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

    def upload_json(
        self,
        data,
        key
    ):

        try:

            self.client.put_object(

                Bucket=S3_BUCKET,

                Key=key,

                Body=convert_to_json(data)

            )

            logger.info(
                f"Uploaded to S3 : {key}"
            )

        except Exception as e:

            raise StorageException(e)