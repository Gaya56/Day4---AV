SELECT
    device_id,
    error_code,
    status,
    last_activity,
    city,
    System.Timestamp AS event_time
INTO
    [outputErrorMonitoring]
FROM
    [inputEventHub]
WHERE
    error_code IS NOT NULL  -- Only include error messages
