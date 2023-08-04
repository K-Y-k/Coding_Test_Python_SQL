/* 문제 분석
(1) 결과 컬럼 : BOOK_ID, PUBLISHED_DATE
(2) 조회 기준 : 2021년에 출판된 '인문' 카테고리에 속하는 데이터
(3) 출판일 기준으로 내림차순 : PUBLISHED_DATE
*/

SELECT BOOK_ID, 
       DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK 
WHERE CATEGORY = '인문' AND YEAR(PUBLISHED_DATE) = 2021
ORDER BY PUBLISHED_DATE DESC