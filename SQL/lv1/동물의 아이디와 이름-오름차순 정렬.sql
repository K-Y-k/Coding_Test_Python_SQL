/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID, NAME
(2) 조회 기준 : 아이디 기준으로 정렬
(3) 아이디 기준으로 오름차순 : ANIMAL_ID
*/

SELECT ANIMAL_ID, 
       NAME 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC