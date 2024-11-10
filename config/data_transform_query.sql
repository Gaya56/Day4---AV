SELECT
    device_id,
    location,
    status,
    last_activity,
    connection,
    city,
    System.Timestamp AS event_time
INTO
    [outputTable]
FROM
    [inputEventHub]
WHERE
    status = 'active'
    location = 'calgary'