/* 문제 분석
(1) 결과 컬럼 : MAX_PRICE
(2) 조회 기준 : 판매 중인 상품 중 가장 높은 판매 가격
*/

SELECT MAX(PRICE) AS MAX_PRICE
FROM PRODUCT