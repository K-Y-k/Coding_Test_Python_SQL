/* 문제 분석
(1) 결과 컬럼 : USER_ID, PRODUCT_ID
(2) 조회 기준 : 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여, 
                재구매한 회원 ID와 재구매한 상품 ID를 출력
(3) 회원 아이디 기준으로 오름차순 : USER_ID
(4) 회원 아이디가 같다면 상품 아이디 기준으로 내림차순 : PRODUCT_ID
*/

SELECT USER_ID,
       PRODUCT_ID
FROM ONLINE_SALE 
GROUP BY USER_ID, PRODUCT_ID 
HAVING COUNT(PRODUCT_ID) >= 2
ORDER BY USER_ID, PRODUCT_ID DESC