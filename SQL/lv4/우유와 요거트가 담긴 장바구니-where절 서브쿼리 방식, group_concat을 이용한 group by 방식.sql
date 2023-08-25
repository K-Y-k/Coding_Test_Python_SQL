/* 문제 분석
(1) 결과 컬럼 : CART_ID
(2) 조회 기준 : 우유와 요거트를 동시에 구입한 장바구니의 아이디
(3) 아이디 기준으로 내림차순 : CART_ID
*/

# 서크쿼리 방식
# SELECT CART_ID
# FROM CART_PRODUCTS 
# WHERE NAME = 'Milk' 
#       AND CART_ID IN (SELECT CART_ID
#                      FROM CART_PRODUCTS
#                      WHERE NAME = 'Yogurt')
# ORDER BY CART_ID


# GROUP_CONCAT으로 그룹으로 묶인 ID의 NAME들을 모두 이어붙여서 LIKE로 찾는 방식
SELECT CART_ID
FROM CART_PRODUCTS
GROUP BY CART_ID
HAVING GROUP_CONCAT(NAME) like '%Milk%' and GROUP_CONCAT(NAME) like '%Yogurt%'
ORDER BY CART_ID