SELECT
    device_id,
    status,
    error_code,        -- Include error code for visibility in Power BI
    last_activity,
    city,
    System.Timestamp AS event_time
INTO
    [outputPowerBI]
FROM
    [inputEventHub]
