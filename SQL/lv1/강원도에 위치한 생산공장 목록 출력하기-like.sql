/* 문제 분석
(1) 결과 컬럼 : FACTORY_ID, FACTORY_NAME, ADDRESS
(2) 조회 기준 : 냉동시설 여부가 NULL인 경우 'N'으로, 
               경기도에 위치
(3) 아이디 기준으로 오름차순 : FACTORY_ID
*/

SELECT FACTORY_ID, 
       FACTORY_NAME, 
       ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '%강원도'
ORDER BY FACTORY_ID