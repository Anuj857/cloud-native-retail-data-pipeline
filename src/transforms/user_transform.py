"""
User Transformation
"""

import pandas as pd

from utils.logger import logger


class UserTransformer:

    @staticmethod
    def transform(data):

        df = pd.json_normalize(data)

        df["full_name"] = (

            df["name.firstname"]

            + " "

            + df["name.lastname"]

        )

        df.rename(

            columns={

                "address.geolocation.lat": "latitude",

                "address.geolocation.long": "longitude"

            },

            inplace=True

        )

        logger.info(
            f"{len(df)} users transformed"
        )

        return df