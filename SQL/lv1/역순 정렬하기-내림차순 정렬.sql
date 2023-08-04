/* 문제 분석
(1) 결과 컬럼 : NAME, DATETIME
(2) 조회 기준 : 아이디 기준으로 역순 정렬
(3) 아이디 기준으로 내림차순 : ANIMAL_ID
*/

SELECT NAME, 
       DATETIME
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID DESC