/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID, NAME, 중성화
(2) 조회 기준 : 동물이 중성화되었는지 아닌지
               중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 
               또는 'Spayed'라는 단어가 들어있음
(3) 아이디 기준으로 오름차순 : ANIMAL_ID
*/

SELECT ANIMAL_ID,
       NAME,
       CASE 
       WHEN SEX_UPON_INTAKE like 'Neutered%' THEN 'O'
       WHEN SEX_UPON_INTAKE like 'Spayed%' THEN 'O' 
       ELSE 'X'
       END AS 중성화
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID