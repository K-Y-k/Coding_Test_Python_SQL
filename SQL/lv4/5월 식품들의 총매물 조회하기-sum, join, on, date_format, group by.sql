/* 문제 분석
(1) 결과 컬럼 : PRODUCT_ID, PRODUCT_NAME, TOTAL_SALES
(2) 조회 기준 : 두 테이블에서 생산일자가 2022년 5월인 식품들
(3) 총매출 기준으로 내림차순 : TOTAL_SALES
(4) 총매출이 같다면 아이디 기준으로 오름차순 : P.PRODUCT_ID
*/

SELECT P.PRODUCT_ID,
       P.PRODUCT_NAME,
       SUM(P.PRICE * O.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT P 
JOIN FOOD_ORDER O
ON P.PRODUCT_ID = O.PRODUCT_ID AND DATE_FORMAT(O.PRODUCE_DATE, '%Y-%m') = '2022-05'
GROUP BY P.PRODUCT_ID, P.PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, P.PRODUCT_ID ASC