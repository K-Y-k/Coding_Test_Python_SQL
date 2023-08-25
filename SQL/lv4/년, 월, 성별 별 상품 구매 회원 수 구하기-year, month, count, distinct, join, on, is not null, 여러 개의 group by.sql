/* 문제 분석
(1) 결과 컬럼 : YEAR, MONTH, GENDER, USERS
(2) 조회 기준 : 두 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계
(3) 년, 월, 성별 기준으로 오름차순 : YEAR, MONTH, I.GENDER
*/

# 동일 회원이 같은달 2회 이상 구매한 경우가 있을 수 있으므로 중복 처리를 해야한다.
SELECT YEAR(S.SALES_DATE) AS YEAR,
       MONTH(S.SALES_DATE) AS MONTH,
       I.GENDER,
       COUNT(DISTINCT S.USER_ID) AS USERS
FROM USER_INFO I
JOIN ONLINE_SALE S
ON I.USER_ID = S.USER_ID AND I.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, I.GENDER
ORDER BY YEAR, MONTH, I.GENDER