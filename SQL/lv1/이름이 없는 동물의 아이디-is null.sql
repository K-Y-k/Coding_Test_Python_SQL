/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID
(2) 조회 기준 : 이름이 없는 채로 들어온 동물
(3) 아이디 기준으로 오름차순 : ANIMAL_ID
*/

SELECT ANIMAL_ID
FROM ANIMAL_INS 
WHERE NAME IS NULL
ORDER BY ANIMAL_ID