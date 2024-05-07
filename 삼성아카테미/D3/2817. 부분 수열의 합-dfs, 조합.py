# 내가 푼 방식 - combinations 활용
# 모든 조합의 경우의 수를 넣어 조건에 해당하는 조건일 때 카운팅 했다.
# 시간 2130ms로 느림

from itertools import combinations
 
T = int(input())
 
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num_li = list(map(int, input().split()))
    answer = 0
 
    for i in num_li:                             # 하나의 숫자인 경우
        if i == K:
            answer += 1
 
    for i in range(2, N+1):                      # 두개 이상의 숫자 합인 경우
        c = combinations(num_li, i)
 
        for j in c:
            if sum(j) == K:
                answer += 1
 
    print('#' + str(test_case), answer)



# dfs 활용 방식
# 주어진 숫자 배열의 각 위취의 숫자를 1.더해준다 와 2.더해주지 않는다를 적용해나감으로써
# 모든 경우의 수를 가져올 수 있고
# 이 때 해당하는 조건과 해당하지 않는 조건을 가지치기를 하며 가려내주면 된다.
# 시간 730ms 더 효율적

from itertools import combinations
 
def dfs(n, total):
    global answer
 
    # 해당하는 조건과 해당하지 않는 조건을 가지치기를 하며 가려내주면 된다.
    if total > K:             # 이미 조건 값을 넘어서면 가지치기
        return
 
    if total == K:            # 조건 값에 해당하면 카운팅하고 가지치기
        answer += 1
        return
 
    if n == N:                # 끝까지 도달하여 넘어서려고 하면 가지치기
        return
     
    dfs(n+1, total+num_li[n]) # 
    dfs(n+1, total)
 
 
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num_li = list(map(int, input().split()))
    answer = 0
 
    dfs(0, 0)                # 첫번째 원소와 합산 값 0으로 초기화
 
    print('#' + str(test_case), answer)


