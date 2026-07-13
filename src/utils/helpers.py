"""
Helper Functions
"""

from datetime import datetime
import json


def current_timestamp():

    return datetime.utcnow().strftime("%Y%m%d_%H%M%S")


def generate_s3_filename(prefix: str):

    timestamp = current_timestamp()

    return f"{prefix}_{timestamp}.json"


def convert_to_json(data):

    return json.dumps(data, indent=4, default=str)