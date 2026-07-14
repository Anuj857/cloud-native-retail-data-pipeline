import sys
import os
import boto3

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from lambda_function import lambda_handler

response = lambda_handler({}, {})

print(response)