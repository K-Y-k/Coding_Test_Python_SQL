/* 문제 분석
(1) 결과 컬럼 : DR_NAME, DR_ID, MCDP_CD, HIRE_YMD
(2) 조회 기준 : 흉부외과(CS)이거나 일반외과(GS)인 데이터만,
               고용일자를 기준으로 내림차순, 
               고용일자가 같다면 이름을 기준으로 오름차순
(3) 고용일자를 기준으로 내림차순 : HIRE_YMD
(4) 고용일자가 같다면 이름을 기준으로 오름차순 : DR_NAME
*/

SELECT DR_NAME, 
       DR_ID, 
       MCDP_CD, 
       DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR 
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME