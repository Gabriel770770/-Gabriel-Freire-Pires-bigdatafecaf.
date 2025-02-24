CREATE VIEW temp_max_min_por_dia AS
SELECT 
    DATE(noted_date) AS data, 
    MAX(temperature) AS temp_max, 
    MIN(temperature) AS temp_min
FROM 
    temperature_readings
GROUP BY 
    DATE(noted_date)
ORDER BY 
    data;