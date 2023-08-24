/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID, ANIMAL_TYPE, NAME
(2) 조회 기준 : 보호소에 들어올 당시에는 중성화 되지 않았지만, 
               보호소를 나갈 당시에는 중성화된 동물
(3) 아이디 기준으로 오름차순 : ANIMAL_ID
*/

SELECT I.ANIMAL_ID,
       I.ANIMAL_TYPE,
       I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID AND I.SEX_UPON_INTAKE LIKE 'Intact%'
WHERE O.SEX_UPON_OUTCOME LIKE 'Spayed%' OR O.SEX_UPON_OUTCOME LIKE 'Neutered%'
ORDER BY I.ANIMAL_ID