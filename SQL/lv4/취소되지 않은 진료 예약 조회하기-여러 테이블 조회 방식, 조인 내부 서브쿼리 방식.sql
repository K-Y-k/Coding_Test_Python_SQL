/* 문제 분석
(1) 결과 컬럼 : APNT_NO, PT_NAME, PT_NO, MCDP_CD, DR_NAME, APNT_YMD
(2) 조회 기준 : 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역
(3) 진료예약일시 기준으로 오름차순 : A.APNT_YMD
*/

# 조회하려는 컬럼이 각 다른 테이블에서의 컬럼이라 FROM절에 3개의 테이블로 조회 방식
SELECT A.APNT_NO,
       P.PT_NAME,
       A.PT_NO,
       A.MCDP_CD,
       D.DR_NAME,
       A.APNT_YMD
FROM PATIENT P, 
     DOCTOR D,
     APPOINTMENT A
WHERE A.PT_NO = P.PT_NO AND A.MDDR_ID = D.DR_ID
      AND DATE_FORMAT(A.APNT_YMD, '%Y-%m-%d') = '2022-04-13' 
      AND A.APNT_CNCL_YN = 'N' AND A.APNT_CNCL_YMD IS NULL
ORDER BY A.APNT_YMD



# 조인 서브쿼리 방식
# SELECT AD.APNT_NO, 
#        P.PT_NAME, 
#        P.PT_NO, 
#        AD.MCDP_CD, 
#        AD.DR_NAME, 
#        AD.APNT_YMD 
# FROM PATIENT P
# JOIN (SELECT A.APNT_NO, 
#              A.MCDP_CD, 
#              D.DR_NAME, 
#              A.APNT_YMD, 
#              A.PT_NO
#       FROM APPOINTMENT A
#       JOIN DOCTOR D
#       ON D.DR_ID = A.MDDR_ID 
#          AND DATE_FORMAT(A.APNT_YMD, '%Y-%m-%d') = '2022-04-13'
#          AND A.APNT_CNCL_YN = 'N' AND A.APNT_CNCL_YMD IS NULL) AD
# ON P.PT_NO = AD.PT_NO
# ORDER BY AD.APNT_YMD;