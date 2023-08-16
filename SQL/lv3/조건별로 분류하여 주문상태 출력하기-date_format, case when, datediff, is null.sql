/* 문제 분석
(1) 결과 컬럼 : ORDER_ID, PRODUCT_ID, OUT_DATE, 출고여부
(2) 조회 기준 : 5월 1일을 기준,
               출고여부는 5월 1일까지 출고완료로 이 후 날짜는 출고 대기로 미정이면 출고미정으로 출력
(3) 주문 아이디 기준으로 오름차순 : ORDER_ID
*/

SELECT ORDER_ID,
       PRODUCT_ID,
       DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
       CASE
       # WHEN DATE_FORMAT(OUT_DATE, '%Y-%m-%d') <= '2022-05-01' THEN '출고완료'
       WHEN DATEDIFF('2022-05-01', OUT_DATE) >= 0 THEN '출고완료'
       WHEN OUT_DATE IS NULL THEN '출고미정'
       ELSE '출고대기'
       END AS 출고여부
FROM FOOD_ORDER 
ORDER BY ORDER_ID