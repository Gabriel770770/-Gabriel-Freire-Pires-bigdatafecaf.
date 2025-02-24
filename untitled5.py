CREATE VIEW leituras_por_hora AS
SELECT 
    EXTRACT(HOUR FROM noted_date) AS hora, 
    COUNT(*) AS contagem
FROM 
    temperature_readings
GROUP BY 
    EXTRACT(HOUR FROM noted_date)
ORDER BY 
    hora;