/* 문제 분석
(1) 결과 컬럼 : NAME, COUNT
(2) 조회 기준 : 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수
(3) 이름 기준으로 오름차순 : NAME
*/

SELECT NAME, 
       COUNT(NAME) AS COUNT
FROM ANIMAL_INS 
GROUP BY NAME HAVING COUNT(NAME) >= 2
ORDER BY NAME