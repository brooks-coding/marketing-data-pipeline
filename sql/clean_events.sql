CREATE OR REPLACE TABLE stg_events AS
SELECT DISTINCT
    event_id,
    user_id,
    event_type,
    event_timestamp,
    campaign_id
FROM events
WHERE user_id IS NOT NULL;