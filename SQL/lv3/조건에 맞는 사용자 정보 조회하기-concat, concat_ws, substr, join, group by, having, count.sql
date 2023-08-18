/* 문제 분석
(1) 결과 컬럼 : USER_ID, NICKNAME, 전체주소, 전화번호
(2) 조회 기준 : 두 테이블에서 중고 거래 게시물을 3건 이상 등록한 사용자
(3) 아이디 기준으로 내림차순 : USER_ID
*/

# CONCAT()은 문자열을 붙이는 것
# CONCAT_WS()은 구분자를 먼저 주고 각 나뉜 문자열들을 이을 때 구분자를 붙여준다.

SELECT U.USER_ID AS USER_ID,
       U.NICKNAME AS NICKNAME,
       CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ' ,U.STREET_ADDRESS2) AS 전체주소,
       CONCAT_WS('-', 
                 SUBSTR(U.TLNO,1,3), SUBSTR(U.TLNO,4,4), SUBSTR(U.TLNO,8,4)) AS 전화번호
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID
GROUP BY USER_ID HAVING COUNT(B.WRITER_ID) > 2
ORDER BY USER_ID DESC