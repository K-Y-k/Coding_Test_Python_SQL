/* 문제 분석
(1) 결과 컬럼 : 시간
(2) 조회 기준 : 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지
*/

SELECT DATETIME AS 시간
FROM ANIMAL_INS 
ORDER By DATETIME ASC LIMIT 1