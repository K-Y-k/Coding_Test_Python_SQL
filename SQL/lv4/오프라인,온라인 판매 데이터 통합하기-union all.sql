/* 문제 분석
(1) 결과 컬럼 : SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
(2) 조회 기준 : 두 테이블에서 2022년 3월의 오프라인/온라인 상품 판매 데이터
(3) 판매일, 상품 아이디, 유저 아이디 순서 기준으로 오름차순 : SALES_DATE, PRODUCT_ID, USER_ID
*/

# 전체 SELECT 테이블에서 UNION 방식
(SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
       PRODUCT_ID,
       USER_ID,
       SALES_AMOUNT
FROM ONLINE_SALE
WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03')

UNION ALL # 일반 UNION은 중복되는 값은 생략하지만 UNION ALL은 중복되는 데이터도 같이 포함시킨다. 

(SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
       PRODUCT_ID,
       NULL AS USER_ID,
       SALES_AMOUNT
FROM OFFLINE_SALE
WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03')
ORDER BY 1, 2, 3



# FROM절에서의 UNION 방식
SELECT DATE_FORMAT(Z.SALES_DATE, '%Y-%m-%d') SALES_DATE,
       Z.PRODUCT_ID,
       Z.USER_ID,
       Z.SALES_AMOUNT
FROM ( SELECT ONLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE FROM ONLINE_SALE
       UNION ALL
       SELECT OFFLINE_SALE_ID, NULL, PRODUCT_ID, SALES_AMOUNT, SALES_DATE FROM OFFLINE_SALE ) Z
WHERE Z.SALES_DATE LIKE '2022-03%'
ORDER BY 1, 2, 3