import pandas as pd

from utils.validator import validate_dataframe


def test_validation():

    df = pd.DataFrame(
        {
            "id": [1],
            "title": ["Laptop"],
            "price": [500],
            "category": ["electronics"]
        }
    )

    validate_dataframe(df)