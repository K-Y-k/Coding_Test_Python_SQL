/* 문제 분석
(1) 결과 컬럼 : USERS
(2) 조회 기준 : 2021년에 가입한 회원 중 
               나이가 20세 이상 29세 이하인 회원이 몇 명인지
*/

SELECT COUNT(*) AS USERS
FROM USER_INFO 
WHERE YEAR(JOINED) = 2021
      AND 
      AGE BETWEEN 20 AND 29