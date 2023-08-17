/* 문제 분석
(1) 결과 컬럼 : CAR_ID
(2) 조회 기준 : 두 테이블에 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차
(3) 아이디 기준으로 내림차순 : CAR_ID
*/

SELECT DISTINCT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
ON C.CAR_ID = H.CAR_ID AND C.CAR_TYPE = '세단' AND MONTH(H.START_DATE) = 10
ORDER BY C.CAR_ID DESC