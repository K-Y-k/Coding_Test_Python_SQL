/* 문제 분석
(1) 결과 컬럼 : HISTORY_ID, CAR_ID, START_DATE, END_DATE, 
               RENT_TYPE
(2) 조회 기준 : 2022년 9월에 속하는 대여 기록이고,
               대여 기간이 30일 이상이면 '장기 대여' 
               그렇지 않으면 '단기 대여'로 표시하는 컬럼을 추가한 데이터
(3) 아이디를 기준으로 내림차순 : HISTORY_ID
*/

SELECT HISTORY_ID,
       CAR_ID,
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       CASE WHEN DATEDIFF(END_DATE, START_DATE) < 29 then '단기 대여'
            ELSE '장기 대여' 
            END AS  RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
 # WHERE START_DATE LIKE '2022-09-%'
WHERE START_DATE BETWEEN '2022-09-01' AND '2022-09-30'
ORDER BY HISTORY_ID DESC