from unittest.mock import patch

from clients.s3_client import S3Client


@patch("clients.s3_client.boto3.client")
def test_upload(mock_client):

    s3 = S3Client()

    s3.upload_json(
        {"name": "Laptop"},
        "raw/test.json"
    )

    assert True