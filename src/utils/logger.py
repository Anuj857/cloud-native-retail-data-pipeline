"""
Centralized Logger
"""

import logging
import sys

LOGGER_NAME = "RetailPipeline"


def get_logger():

    logger = logging.getLogger(LOGGER_NAME)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(filename)s | %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.propagate = False

    return logger


logger = get_logger()