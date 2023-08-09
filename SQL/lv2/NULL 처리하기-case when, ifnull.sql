/* 문제 분석
(1) 결과 컬럼 : ANIMAL_TYPE, NAME, SEX_UPON_INTAKE
(2) 조회 기준 : 이름이 없는 동물의 이름은 "No name"으로 표시
(3) 아이디 기준으로 오름차순 : ANIMAL_ID
*/

SELECT ANIMAL_TYPE,
       CASE WHEN NAME IS NULL THEN 'No name'
       ELSE NAME 
       END AS NAME,
       SEX_UPON_INTAKE
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID

# SELECT ANIMAL_TYPE,
#        IFNULL(NAME, 'No name') AS NAME,
#        SEX_UPON_INTAKE
# FROM ANIMAL_INS 
# ORDER BY ANIMAL_ID