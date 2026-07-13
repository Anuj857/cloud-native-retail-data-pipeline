from unittest.mock import MagicMock
from unittest.mock import patch

import pandas as pd

from clients.dynamodb_client import DynamoDBClient


@patch("clients.dynamodb_client.boto3.resource")
def test_insert(mock_resource):

    table = MagicMock()

    resource = MagicMock()

    resource.Table.return_value = table

    mock_resource.return_value = resource

    client = DynamoDBClient()

    df = pd.DataFrame(
        [
            {
                "id": 1,
                "title": "Laptop",
                "price": 1000,
                "category": "electronics",
                "rating_rate": 4.5,
                "rating_count": 10,
            }
        ]
    )

    client.batch_insert(df)

    assert table.batch_writer.called