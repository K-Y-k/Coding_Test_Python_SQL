/* 문제 분석
(1) 결과 컬럼 : PRICE_GROUP, PRODUCTS
(2) 조회 기준 : 만원 단위의 가격대 별로 상품 개수를 출력
               최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000)으로 표시
(3) 가격대 기준으로 오름차순 : PRICE_GROUP
*/

SELECT TRUNCATE(PRICE, -4) AS PRICE_GROUP,
       COUNT(PRICE) AS PRODUCTS
FROM PRODUCT 
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP