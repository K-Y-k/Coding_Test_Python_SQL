/* 문제 분석
(1) 결과 컬럼 : HOUR, COUNT
(2) 조회 기준 : 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지
(3) 시간대 기준으로 오름차순 : HOUR
*/

WITH RECURSIVE R AS (              # 재귀쿼리 세팅
    (SELECT 0 AS HOUR)             # 초기값 설정
    UNION ALL                      # 위 쿼리와 아래 쿼리의 값을 연산
    (SELECT HOUR + 1 
     FROM R                        # 하나씩 불려 나감 
     WHERE HOUR < 23)              # 반복을 멈추는 용도
)

SELECT R.HOUR AS HOUR,
       COUNT(O.ANIMAL_ID) AS COUNT # ANIMAL_OUTS의 컬럼 아무거나 넣으면 된다. 
                                   # R 테이블의 시간에서 ANIMAL_OUTS의 컬럼 값이 있는지 조회하면 되므로  
FROM R
LEFT JOIN ANIMAL_OUTS O            # 각 시간에 ANIMAL_OUTS의 데이터가 없으면 빈 데이터로 넣어야 하므로 left join 사용
ON R.HOUR = HOUR(O.DATETIME)
GROUP BY R.HOUR
ORDER BY 1