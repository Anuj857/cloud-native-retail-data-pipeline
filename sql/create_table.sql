CREATE EXTERNAL TABLE IF NOT EXISTS retail_products_curated (
    id INT,
    title STRING,
    price DOUBLE,
    description STRING,
    category STRING,
    image STRING,
    rating STRUCT<
        rate: DOUBLE,
        count: INT
    >
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://retail-raw-datalake-anuj857/curated/products/';