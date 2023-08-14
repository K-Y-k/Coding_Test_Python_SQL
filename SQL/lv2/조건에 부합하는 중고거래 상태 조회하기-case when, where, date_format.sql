/* 문제 분석
(1) 결과 컬럼 : BOARD_ID, WRITER_ID, TITLE, PRICE, STATUS
(2) 조회 기준 : 2022년 10월 5일에 등록된 중고거래 게시물,
                거래상태가 SALE 이면 판매중, RESERVED이면 예약중, DONE이면 거래완료 분류하여 출력
(3) 게시글 아이디 기준으로 내림차순 : BOARD_ID
*/

SELECT BOARD_ID,
       WRITER_ID,
       TITLE,
       PRICE,
       CASE 
       WHEN STATUS = 'DONE' THEN '거래완료'
       WHEN STATUS = 'RESERVED' THEN '예약중'
       ELSE '판매중'
       END AS STATUS
FROM USED_GOODS_BOARD 
WHERE DATE_FORMAT(CREATED_DATE, '%Y-%m-%d') = '2022-10-05'
ORDER BY BOARD_ID DESC