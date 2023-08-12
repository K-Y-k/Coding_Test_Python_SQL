/* 문제 분석
(1) 결과 컬럼 : ANIMAL_ID, NAME, SEX_UPON_INTAKE
(2) 조회 기준 :  이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 데이터만
(3) 아이디 기준으로 오름차순 : ANIMAL_ID
*/

SELECT ANIMAL_ID,
       NAME,
       SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
ORDER BY ANIMAL_ID