SELECT
    device_id,
    status,
    last_activity,
    event_time,
    city
INTO
    outputPowerBI
FROM
    inputEventHub
WHERE
    status IN ('active', 'inactive') AND city = 'Calgary';
