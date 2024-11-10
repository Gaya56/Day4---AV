SELECT
    device_id,
    status,
    error_code,
    event_time
INTO
    outputPowerBI, outputDataActivator
FROM
    inputEventStream
WHERE
    error_code IS NOT NULL;  -- Only route error messages
