-- stream that takes data from products topic
CREATE STREAM products_raw_data (
    barcode VARCHAR,
    category VARCHAR,
    name VARCHAR,
    price VARCHAR,
    description VARCHAR
) WITH (
    KAFKA_TOPIC = 'products',
    VALUE_FORMAT = 'AVRO'
);

-- stream that filters stream of products raw data by category and selects only products from food category
CREATE STREAM products_from_food_category AS
    SELECT
        barcode,
        category,
        name,
        price,
        description
    FROM products_raw_data
    WHERE category = 'Food'
    EMIT CHANGES;

-- ktable that stores amount of products of each category for the last five minutes with shifting every minute
CREATE TABLE amount_of_products_by_category_for_the_last_five_minute AS
    SELECT
        category,
        COUNT(category) as count
    FROM products_raw_data
    WINDOW HOPPING (SIZE 5 MINUTES, ADVANCE BY 1 MINUTE)
    GROUP BY category
    EMIT CHANGES;