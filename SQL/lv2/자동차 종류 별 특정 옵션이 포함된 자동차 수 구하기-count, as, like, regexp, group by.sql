/* 문제 분석
(1) 결과 컬럼 : CAR_TYPE, CARS
(2) 조회 기준 : '통풍시트', '열선시트', '가죽시트' 중 
               하나 이상의 옵션이 포함된 자동차
(3) 자동차 종류 기준으로 오름차순 : CAR_TYPE
*/

SELECT CAR_TYPE,
       COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
# WHERE OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%가죽시트%'
WHERE options REGEXP '통풍시트|열선시트|가죽시트'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE