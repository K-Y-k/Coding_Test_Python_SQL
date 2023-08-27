/* 문제 분석
(1) 결과 컬럼 : MEMBER_NAME, REVIEW_TEXT, REVIEW_DATE
(2) 조회 기준 : 두 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들
(3) 리뷰 작성일 기준으로 오름차순 : REVIEW_DATE
(4) 리뷰 작성일이 같다면 리뷰 텍스트 기준으로 오름차순 : R.REVIEW_TEXT
*/

SELECT P.MEMBER_NAME,
       R.REVIEW_TEXT,
       DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE P
JOIN REST_REVIEW R
ON P.MEMBER_ID = R.MEMBER_ID
WHERE P.MEMBER_ID = (SELECT A.MEMBER_ID
                     FROM MEMBER_PROFILE A
                     JOIN REST_REVIEW B
                     ON A.MEMBER_ID = B.MEMBER_ID
                     GROUP BY A.MEMBER_ID
                     ORDER BY COUNT(A.MEMBER_ID) DESC
                     LIMIT 1)
ORDER BY 3, 2