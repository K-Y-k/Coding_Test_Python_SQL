/* 문제 분석
(1) 결과 컬럼 : ANIMAL_TYPE, count
(2) 조회 기준 :  고양이와 개가 각각 몇 마리인지
(3) 동물 종류 기준으로 오름차순 : ANIMAL_TYPE
*/

SELECT ANIMAL_TYPE,	
       COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE