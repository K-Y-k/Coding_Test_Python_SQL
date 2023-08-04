/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID, NAME, DATETIME
(2) 조회 기준 : 이름 순, 
               이름이 같은 경우 보호를 나중에 시작한 동물을 먼저
(3) 이름 기준으로 오름차순 : NAME
(4) 이름이 같은 경우 보호를 나중에 시작한 동물 기준으로 내림차순 : DATETIME
*/

SELECT ANIMAL_ID,
       NAME, 
       DATETIME 
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC