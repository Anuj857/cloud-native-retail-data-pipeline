import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")

S3_BUCKET = os.getenv("BUCKET_NAME")

DYNAMODB_TABLE = os.getenv("TABLE_NAME")

PRODUCT_API = "https://fakestoreapi.com/products"

USER_API = "https://fakestoreapi.com/users"

REQUEST_TIMEOUT = 10

MAX_RETRIES = 3

BACKOFF_FACTOR = 2

RAW_PRODUCTS_PATH = "raw/products"

RAW_USERS_PATH = "raw/users"