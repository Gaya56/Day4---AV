SELECT
    device_id,
    status,
    last_activity,
    city,
    System.Timestamp AS event_time
INTO
    [outputPowerBI]
FROM
    [inputEventHub]
WHERE
    city = 'Calgary'
