SELECT 
    CAR_TYPE,
    COUNT(CAR_ID) AS CARS  -- 자동차 수를 세고 컬럼명을 'CARS'로 지정
FROM 
    CAR_RENTAL_COMPANY_CAR
WHERE 
    -- '통풍시트', '열선시트', '가죽시트' 중 하나 이상이 포함된 경우를 정규표현식으로 찾음
    OPTIONS REGEXP '통풍시트|열선시트|가죽시트' 
GROUP BY 
    CAR_TYPE  -- 자동차 종류별로 그룹화
ORDER BY 
    CAR_TYPE ASC;  -- 자동차 종류 기준 오름차순 정렬