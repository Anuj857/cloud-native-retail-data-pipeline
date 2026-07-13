"""
Product Transformation
"""

import pandas as pd

from utils.logger import logger
from utils.validator import (
    validate_dataframe,
    validate_price,
    remove_duplicates,
    fill_missing
)


class ProductTransformer:

    @staticmethod
    def transform(data):

        df = pd.json_normalize(data)

        df.rename(

            columns={

                "rating.rate": "rating_rate",

                "rating.count": "rating_count"

            },

            inplace=True

        )

        df = remove_duplicates(df)

        df = fill_missing(df)

        df["price"] = df["price"].astype(float)

        validate_dataframe(df)

        validate_price(df)

        logger.info(
            f"{len(df)} products transformed"
        )

        return df