/* 문제 분석
(1) 결과 컬럼 : I.FLAVOR
(2) 조회 기준 : 총주문량이 3,000보다 높으면서 
               주 성분이 과일인 아이스크림을 총주문량이 큰 순서대로
(3) 총주문량을 기준으로 내림차순 : AGE
*/

SELECT I.FLAVOR
FROM ICECREAM_INFO AS I 
LEFT JOIN FIRST_HALF AS F
ON I.FLAVOR = F.FLAVOR
WHERE I.INGREDIENT_TYPE = 'fruit_based' AND F.TOTAL_ORDER > 3000
ORDER BY F.TOTAL_ORDER DESC;