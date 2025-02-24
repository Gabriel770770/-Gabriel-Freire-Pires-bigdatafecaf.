CREATE VIEW avg_temp_por_dispositivo AS
SELECT 
    device_id, 
    AVG(temperature) AS avg_temp
FROM 
    temperature_readings
GROUP BY 
    device_id;