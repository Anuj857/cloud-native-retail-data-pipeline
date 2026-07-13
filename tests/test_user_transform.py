from transforms.user_transform import UserTransformer


def test_user_transform():

    sample = [
        {
            "id": 1,
            "name": {
                "firstname": "Anuj",
                "lastname": "Yadav"
            },
            "address": {
                "geolocation": {
                    "lat": "22",
                    "long": "75"
                }
            }
        }
    ]

    df = UserTransformer.transform(sample)

    assert len(df) == 1

    assert "full_name" in df.columns