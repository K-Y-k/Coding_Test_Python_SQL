/* 문제 분석
(1) 결과 컬럼 : FLAVOR
(2) 조회 기준 : 총주문량을 기준으로 내림차순 정렬,
               총주문량이 같다면 출하 번호를 기준으로 오름차순 정렬
(3) 총주문량을 기준으로 내림차순 : TOTAL_ORDER
(4) 총주문량이 같다면 출하 번호를 기준으로 오름차순 : SHIPMENT_ID
*/

SELECT FLAVOR
FROM FIRST_HALF 
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID