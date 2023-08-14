/* 문제 분석
(1) 결과 컬럼 : CAR_ID, AVERAGE_DURATION
(2) 조회 기준 : 평균 대여 기간이 7일 이상인 자동차들,
                평균 대여 기간은 소수점 두번째 자리에서 반올림
(3) 평균 대여 기간 기준으로 내림차순 : AVERAGE_DURATION
(4) 평균 대여 기간이 같으면 아이디 기준으로 내림차순 : CAR_ID
*/

SELECT CAR_ID,
       ROUND(AVG(DATEDIFF(END_DATE,START_DATE)+1),1) AS AVERAGE_DURATION
       # 시작한 날짜부터 적용되므로 +1을 해줘야 한다.
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
GROUP BY CAR_ID 
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC