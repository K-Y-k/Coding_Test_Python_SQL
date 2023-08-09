/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID, NAME, 날짜
(2) 조회 기준 : 날짜 형태를 년-월-일 형태로 변환하기
(3) 아이디 기준으로 오름차순 : ANIMAL_ID
*/

SELECT ANIMAL_ID,
       NAME,
       DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID