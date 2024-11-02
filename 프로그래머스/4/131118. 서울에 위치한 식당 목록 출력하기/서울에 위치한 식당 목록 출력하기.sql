SELECT 
    a.REST_ID, 
    a.REST_NAME, 
    a.FOOD_TYPE, 
    a.FAVORITES, 
    a.ADDRESS, 
    ROUND(AVG(b.REVIEW_SCORE), 2) AS SCORE
FROM 
    REST_INFO AS a
LEFT JOIN 
    REST_REVIEW AS b
ON 
    a.REST_ID = b.REST_ID
WHERE 
    a.ADDRESS LIKE '서울%'
GROUP BY 
    a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS
HAVING 
    SCORE IS NOT NULL
    
ORDER BY 
    SCORE DESC, a.FAVORITES DESC;