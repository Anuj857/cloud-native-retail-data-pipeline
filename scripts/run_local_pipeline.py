import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from src.clients.api_client import APIClient

from src.transforms.product_transform import ProductTransformer

from src.config import PRODUCT_API

client = APIClient()

products = client.fetch(PRODUCT_API)

df = ProductTransformer.transform(products)

print(df.head())

print()

print(df.info())