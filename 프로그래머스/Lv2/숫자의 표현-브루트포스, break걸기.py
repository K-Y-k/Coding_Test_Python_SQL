# 처음에는 문제에서 방법의 수를 원하여 dp로 접근하였지만 규칙이 나오지 않았다..

# 문제에서 연속된 값만 가능하다고 했으므로
# 1~n까지 각 위치에서부터 연속 합을 하여 동일할 때 카운트를 세주고 현재 루프에서는 용무가 끝났으므로 break

# 주의점은 동일할 때만 break을 걸면 효율성 테스트에서 실행초과가 발생한다.
# 예상으로는 동일 값이 안 나오고 합의 값이 n보다 큰 상황인데도 계속 루프를 진행하는 것이 비효율이기에 발생한 것 같다.
# 즉, 꼭 따로 조건절로 n보다 큰 경우에도 break을 걸어주자.


def solution(n):
    count = 0
    
    for i in range(1, n+1):
        total = 0
        
        for j in range(i, n+1):     # 1~n까지 각 위치에서부터 연속 합을 하여
            total += j
            
            if total == n:          # 동일할 때 카운트를 세주면 된다.
                count += 1
                break
            elif total > n:         # 꼭 따로 조건절로 n보다 큰 경우에도 break을 걸어주자.
                break
    
    return count