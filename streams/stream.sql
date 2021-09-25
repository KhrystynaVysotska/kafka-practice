-- stream that takes raw data from customers topic
CREATE STREAM customers_raw_data (
    email VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    age INT,
    address VARCHAR,
    gender VARCHAR,
    job VARCHAR,
    has_children_under_sixteen BOOLEAN
) WITH (
    KAFKA_TOPIC='customers',
    VALUE_FORMAT='AVRO'
);

-- stateless stream that uses data from customers_raw_data (created above) and filters customers by their age
CREATE STREAM adult_customers AS
    SELECT
        email,
        first_name,
        last_name,
        age,
        address,
        gender,
        job,
        has_children_under_sixteen
    FROM customers_raw_data
    WHERE age >= 18
    EMIT CHANGES;

-- ktable that stores aggregated data about customers: number of males and females in stream per minute
CREATE TABLE amount_of_users_by_gender_for_the_last_minute AS
    SELECT
        gender,
        COUNT(gender) as count
    FROM customers_raw_data
    WINDOW TUMBLING (SIZE 1 MINUTE, GRACE PERIOD 2 HOURS)
    GROUP BY gender
    EMIT CHANGES;

-- stream that takes customers who have small children and may be potentially interested in buying toys
CREATE STREAM customers_interesting_in_buying_toys AS
    SELECT
        email,
        first_name,
        last_name,
        age,
        address,
        gender,
        job,
        has_children_under_sixteen
    FROM customers_raw_data
    WHERE has_children_under_sixteen=True
    EMIT CHANGES;