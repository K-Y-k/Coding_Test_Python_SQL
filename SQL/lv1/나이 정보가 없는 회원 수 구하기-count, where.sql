/* 문제 분석
(1) 결과 컬럼 : COUNT(*)
(2) 조회 기준 : 나이 정보가 없는 회원이 몇 명인지
*/

SELECT COUNT(*)
FROM USER_INFO
WHERE AGE IS NULL