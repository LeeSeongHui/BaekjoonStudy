-- 코드를 입력하세요
SELECT TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) HOUR, COUNT(DATETIME) COUNT
FROM ANIMAL_OUTS
WHERE TO_CHAR(DATETIME, 'HH24:SS') BETWEEN '09:00' AND '19:59' 
GROUP BY TO_CHAR(DATETIME, 'HH24')
ORDER BY 1