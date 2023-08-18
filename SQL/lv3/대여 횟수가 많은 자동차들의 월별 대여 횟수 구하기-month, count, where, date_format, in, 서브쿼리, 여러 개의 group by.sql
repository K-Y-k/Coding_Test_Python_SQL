/* 문제 분석
(1) 결과 컬럼 : MONTH, CAR_ID, RECORDS
(2) 조회 기준 : 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서 
               해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력
(3) 월 기준으로 오름차순 : CAR_ID
(3) 월이 같다면 아이디 기준으로 내림차순 : CAR_ID
*/

SELECT MONTH(START_DATE) AS MONTH,
       CAR_ID,
       COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
      AND CAR_ID IN (SELECT CAR_ID 
                     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                     WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
                     GROUP BY CAR_ID
                     HAVING COUNT(*) >= 5)
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID DESC