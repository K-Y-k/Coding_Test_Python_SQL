/* 문제 분석
(1) 결과 컬럼 : CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS 
(2) 조회 기준 : '네비게이션' 옵션이 포함된 자동차 리스트
(3) 아이디를 기준으로 내림차순 : CAR_ID
*/

SELECT CAR_ID, 
       CAR_TYPE, 
       DAILY_FEE, 
       OPTIONS 
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC