/* 문제 분석
(1) 결과 컬럼 : B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID,
               R.CONTENTS, CREATED_DATE
(2) 조회 기준 : 2022년 10월에 작성된 게시글이고,
               댓글 작성일을 기준으로 오름차순,
               댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순
(3) 댓글 작성일을 기준으로 오름차순 : R.CREATED_DATE
(4) 댓글 작성일이 같다면 제목을 기준으로 오름차순 : B.TITLE
*/

SELECT B.TITLE,
       B.BOARD_ID,
       R.REPLY_ID,
       R.WRITER_ID,
       R.CONTENTS,
       DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS B 
INNER 
JOIN USED_GOODS_REPLY AS R
ON B.BOARD_ID = R.BOARD_ID
# WHERE B.CREATED_DATE LIKE '2022-10-%'
WHERE B.CREATED_DATE BETWEEN '2022-10-01' AND '2022-10-31'
# WHERE SUBSTR(B.CREATED_DATE, 1, 7) = '2022-10'
ORDER BY R.CREATED_DATE ASC, B.TITLE ASC;