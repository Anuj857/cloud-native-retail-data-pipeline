"""
Validation Utilities
"""

import pandas as pd

from utils.exceptions import ValidationException


REQUIRED_PRODUCT_COLUMNS = [

    "id",

    "title",

    "price",

    "category"

]


def validate_dataframe(df: pd.DataFrame):

    if df.empty:

        raise ValidationException("DataFrame is empty.")

    for column in REQUIRED_PRODUCT_COLUMNS:

        if column not in df.columns:

            raise ValidationException(
                f"Missing column : {column}"
            )


def validate_price(df: pd.DataFrame):

    if (df["price"] < 0).any():

        raise ValidationException(
            "Negative product price detected."
        )


def remove_duplicates(df: pd.DataFrame):

    return df.drop_duplicates()


def fill_missing(df: pd.DataFrame):

    df.fillna(
        {
            "title": "Unknown",

            "category": "Others",

            "description": "",

            "price": 0
        },
        inplace=True
    )

    return df