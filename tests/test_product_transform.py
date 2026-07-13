from transforms.product_transform import ProductTransformer


def test_product_transform():

    sample = [
        {
            "id": 1,
            "title": "Laptop",
            "price": 25000,
            "category": "electronics",
            "rating": {
                "rate": 4.5,
                "count": 50
            }
        }
    ]

    df = ProductTransformer.transform(sample)

    assert len(df) == 1

    assert "rating_rate" in df.columns

    assert "rating_count" in df.columns