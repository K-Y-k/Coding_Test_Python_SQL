/* 문제 분석
(1) 결과 컬럼 : NAME, DATETIME
(2) 조회 기준 : 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리
(3) 보호 시작일 기준으로 오름차순 : I.DATETIME
*/

SELECT I.NAME,
       I.DATETIME
FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O             # LEFT JOIN으로 보호소에 있는 테이블에는 있지만
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL           # 입양나간 테이블에는 없는 값만 뽑아낸 것
ORDER BY I.DATETIME
LIMIT 3