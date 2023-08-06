/* 문제 분석
(1) 결과 컬럼 : count
(2) 조회 기준 : 중복을 제외한 동물 보호소에 들어온 동물의 이름은 몇 개인지
*/

SELECT COUNT(DISTINCT NAME) AS count
FROM ANIMAL_INS