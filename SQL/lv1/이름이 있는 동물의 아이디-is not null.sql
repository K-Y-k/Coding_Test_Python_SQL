/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID
(2) 조회 기준 : 이름이 있는 동물
(3) 아이디 기준으로 오름차순 : ANIMAL_ID
*/

SELECT ANIMAL_ID
FROM ANIMAL_INS 
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID