/* 문제 분석
(1) 결과 컬럼 : PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, 
               CATEGORY, PRICE
(2) 조회 기준 : 가격이 제일 비싼 식품 조회
*/

SELECT PRODUCT_ID,	
       PRODUCT_NAME,
       PRODUCT_CD,
       CATEGORY,
       PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1