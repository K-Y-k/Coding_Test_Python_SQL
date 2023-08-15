/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID, NAME
(2) 조회 기준 : 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 2마리
(3) 보호 기간 기준으로 내림차순 : DATEDIFF(O.DATETIME, I.DATETIME)
*/

SELECT I.ANIMAL_ID,
       I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC
LIMIT 2