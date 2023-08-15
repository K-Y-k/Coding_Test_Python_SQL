/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID, NAME
(2) 조회 기준 : 관리자의 실수로 일부 동물의 입양일이 잘못 입력되어
               보호 시작일보다 입양일이 더 빠른 동물만
(3) 보호 시작일 기준으로 오름차순 : I.DATETIME
*/

SELECT I.ANIMAL_ID,
       I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID AND I.DATETIME > O.DATETIME
ORDER BY I.DATETIME