/* 문제 분석
(1) 결과 컬럼 : PT_NAME, PT_NO, GEND_CD, AGE, TLNO
(2) 조회 기준 : 전화번호가 없는 경우 'NONE'으로,
               12세 이하인 여자환자
(3) 나이를 기준으로 내림차순 : AGE
(4) 나이가 같다면 이름을 기준으로 오름차순 : PT_NAME
*/

SELECT PT_NAME,
       PT_NO, 
       GEND_CD, 
       AGE, 
       IF(TLNO IS NULL, 'NONE', TLNO) AS TLNO
FROM PATIENT 
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME