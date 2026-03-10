CREATE OR REPLACE TABLE stg_users AS
SELECT DISTINCT
    user_id,
    signup_date,
    COALESCE(country, 'unknown') AS country,
    marketing_source
FROM users
WHERE user_id IS NOT NULL;