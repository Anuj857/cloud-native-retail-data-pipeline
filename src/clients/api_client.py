"""
API Client
Handles API requests with retry logic and exponential backoff.
"""

import time
import requests

from utils.logger import logger
from utils.exceptions import APIException

from config import (
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    BACKOFF_FACTOR
)


class APIClient:

    def __init__(self):
        self.session = requests.Session()

    def fetch(self, url: str):

        retry = 0

        while retry < MAX_RETRIES:

            try:

                logger.info(f"Fetching : {url}")

                response = self.session.get(
                    url,
                    timeout=REQUEST_TIMEOUT
                )

                response.raise_for_status()

                logger.info("API Request Successful")

                return response.json()

            except requests.exceptions.RequestException as e:

                retry += 1

                logger.warning(
                    f"Retry {retry}/{MAX_RETRIES}"
                )

                if retry == MAX_RETRIES:

                    raise APIException(
                        f"API Failed : {e}"
                    )

                time.sleep(BACKOFF_FACTOR ** retry)