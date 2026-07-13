import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = boto3.Session().region_name or "ap-south-1"

S3_BUCKET = os.getenv("BUCKET_NAME")

DYNAMODB_TABLE = os.getenv("TABLE_NAME")

PRODUCT_API = "https://fakestoreapi.com/products"

USER_API = "https://fakestoreapi.com/users"

REQUEST_TIMEOUT = 10

MAX_RETRIES = 3

BACKOFF_FACTOR = 2

RAW_PRODUCTS_PATH = "raw/products"

RAW_USERS_PATH = "raw/users"