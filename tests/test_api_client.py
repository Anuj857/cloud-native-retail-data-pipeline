from unittest.mock import patch

from clients.api_client import APIClient


@patch("clients.api_client.requests.Session.get")
def test_fetch_products(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = [
        {
            "id": 1,
            "title": "Laptop"
        }
    ]

    client = APIClient()

    result = client.fetch("https://fakeapi.com")

    assert result[0]["id"] == 1

    assert result[0]["title"] == "Laptop"