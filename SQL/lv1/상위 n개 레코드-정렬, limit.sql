/* 문제 분석
(1) 결과 컬럼 : NAME
(2) 조회 기준 : 가장 먼저 들어온 동물 기준으로, 
               1개의 데이터만
(3) 가장 먼저 들어온 동물 기준으로 오름차순 : DATETIME
*/

SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME 
LIMIT 1