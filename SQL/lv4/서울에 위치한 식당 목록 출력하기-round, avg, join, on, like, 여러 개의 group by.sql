/* 문제 분석
(1) 결과 컬럼 : REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
(2) 조회 기준 : 두 테이블에서 서울에 위치한 식당들,
            이때 리뷰 평균점수는 소수점 세 번째 자리에서 반올림      
(3) 평균점수 기준으로 내림차순 : SCORE
(4) 평균점수 같다면 즐겨찾기수 기준으로 내림차순 : I.FAVORITES
*/

SELECT I.REST_ID,
       I.REST_NAME,
       I.FOOD_TYPE,
       I.FAVORITES,
       I.ADDRESS,
       ROUND(AVG(R.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO I
JOIN REST_REVIEW R
ON I.REST_ID = R.REST_ID AND I.ADDRESS LIKE '서울%'
GROUP BY 1,2,3,4,5  # I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS
ORDER BY SCORE DESC, I.FAVORITES DESC