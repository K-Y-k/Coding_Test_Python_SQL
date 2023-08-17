/* 문제 분석
(1) 결과 컬럼 : FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
(2) 조회 기준 : 음식종류별로 즐겨찾기수가 가장 많은 식당
(3) 음식 종류 기준으로 내림차순 : FOOD_TYPE
*/

# WHERE절 서브쿼리 방식
# SELECT *
# FROM 테이블명
# WHERE (컬럼1, 컬럼2) IN (SELECT 서브쿼리_컬럼1, 서브쿼리_컬럼2 FROM 서브쿼리_테이블);
SELECT FOOD_TYPE, 
       REST_ID, 
       REST_NAME, 
       FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES) 
                                 FROM REST_INFO 
                                 GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC


# FROM절 서브쿼리 방식
# SELECT A.FOOD_TYPE, 
#        A.REST_ID, 
#        A.REST_NAME, 
#        A.FAVORITES
# FROM REST_INFO A,
#      (SELECT FOOD_TYPE, 
#              MAX(FAVORITES) AS FAVORITES
#       FROM REST_INFO
#       GROUP BY FOOD_TYPE) B
# WHERE A.FOOD_TYPE = B.FOOD_TYPE AND A.FAVORITES = B.FAVORITES
# ORDER BY FOOD_TYPE DESC



# 잘못된 방식
# SELECT FOOD_TYPE,
#        REST_ID,
#        REST_NAME,
#        MAX(FAVORITES)  # GROUP BY는 같이 묶은 컬럼을 하나의 행으로 표현하는데 
                         # MAX는 표현된 행들 중에서 최대값을 불러오는 것이라 이렇게 안되는 것이다.
# FROM REST_INFO
# GROUP BY FOOD_TYPE
# ORDER BY FOOD_TYPE DESC