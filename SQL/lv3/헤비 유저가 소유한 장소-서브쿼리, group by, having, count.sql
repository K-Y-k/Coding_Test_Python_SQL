/* 문제 분석
(1) 결과 컬럼 : ID, NAME, HOST_ID
(2) 조회 기준 : 공간 테이블에 공간을 둘 이상 등록한 사람
(3) 아이디 기준으로 오름차순 : ID
*/

# WHERE절 서브쿼리
SELECT * 
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID 
                  FROM PLACES
                  GROUP BY HOST_ID
                  HAVING COUNT(HOST_ID) > 1)
ORDER BY ID


# FROM절 서브쿼리
# SELECT A.*
# FROM PLACES A,
#      (SELECT HOST_ID
#       FROM PLACES
#       GROUP BY HOST_ID HAVING COUNT(*) >= 2) B
# WHERE A.HOST_ID = B.HOST_ID
# ORDER BY A.ID