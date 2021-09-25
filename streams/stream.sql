-- stream that takes data from users topic where raw data is stored
CREATE STREAM users_input (
    email VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    age INT,
    address VARCHAR,
    gender VARCHAR,
    job VARCHAR,
    has_children_under_sixteen BOOLEAN
) WITH (
    KAFKA_TOPIC='users',
    VALUE_FORMAT='AVRO'
);

-- stateless stream that uses data from users_input (created above) and filters users by their age
CREATE STREAM adult_users AS
    SELECT
        email,
        first_name,
        last_name,
        age,
        address,
        gender,
        job,
        has_children_under_sixteen
    FROM users_input
    WHERE age >= 18
    EMIT CHANGES;

-- ktable that stores aggregated data about users: number of males and females in stream per minute
CREATE TABLE count_users_by_gender AS
    SELECT
        gender,
        COUNT(gender) as count
    FROM users_input
    WINDOW TUMBLING (SIZE 1 MINUTE, GRACE PERIOD 2 HOURS)
    GROUP BY gender
    EMIT CHANGES;