/* 문제 분석
(1) 결과 컬럼 : FLAVOR
(2) 조회 기준 : 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛
(3) 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량 기준으로 내림차순 : SUM(F.TOTAL_ORDER + J.TOTAL_ORDER)
*/

SELECT F.FLAVOR
FROM FIRST_HALF F
JOIN JULY J
ON F.FLAVOR = J.FLAVOR   # 맛을 기준으로 조인해야 정상적으로 조회됨
GROUP BY F.FLAVOR
ORDER BY SUM(F.TOTAL_ORDER + J.TOTAL_ORDER) DESC
LIMIT 3
