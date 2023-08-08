/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID, NAME
(2) 조회 기준 : 이름에 "EL"이 들어가는 개
(3) 이름 기준으로 오름차순 : NAME
*/

SELECT ANIMAL_ID,
       NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME