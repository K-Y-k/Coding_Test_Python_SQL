/* 문제 분석
(1) 결과 컬럼 : CATEGORY, MAX_PRICE, PRODUCT_NAME
(2) 조회 기준 : 식품분류별로 가격이 제일 비싼 식품
(3) 최대 가격 기준으로 내림차순 : MAX_PRICE
*/

# GROUP BY로 묶인 것과 GROUP BY 관련 함수인 MAX(PRICE) 부분만 관련된 데이터가 나오고
# PRODUCT_NAME은 관련이 없는 값이 나올 수 있다.

# SELECT CATEGORY,
#        MAX(PRICE) AS MAX_PRICE,
#        PRODUCT_NAME
# FROM FOOD_PRODUCT
# GROUP BY CATEGORY 
# HAVING CATEGORY IN ('과자', '국', '김치', '식용유') 
# ORDER BY MAX_PRICE DESC


# 그래서 서브쿼리로 PRICE 최대 값인 것인 데이터들을 조회한 후에
# GROUP BY로 묶어서 관련된 데이터만 나오게 한다.

SELECT CATEGORY, 
       PRICE AS MAX_PRICE, 
       PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE CATEGORY IN ('과자', '국', '김치', '식용유') 
      AND PRICE IN (SELECT MAX(PRICE)  
                    FROM FOOD_PRODUCT 
                    GROUP BY CATEGORY)
GROUP BY CATEGORY
ORDER BY MAX_PRICE DESC