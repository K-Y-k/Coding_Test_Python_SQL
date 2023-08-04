/* 문제 분석
(1) 결과 컬럼 : 시간
(2) 조회 기준 : 가장 최근에 들어온 동물은 언제 들어왔는지
*/

SELECT MAX(DATETIME) as 시간
FROM ANIMAL_INS