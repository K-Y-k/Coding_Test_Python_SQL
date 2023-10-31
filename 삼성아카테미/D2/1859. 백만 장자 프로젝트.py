# 내가 시도한 방식 = 일부 테케 실패
# 루프를 돌려 현재 위치의 값에서부터 끝의 값까지 조회하여 더 큰 값이 있으면
# 큰 값을 최신화하고
# 큰 값이 있었으면 가격 차이를 정답에 더해준다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    coin_li = list(map(int, input().split()))
    answer = 0

    for i in range(N):                         # 현재 위치의 값에서부터
        max_count = 0
        
        for j in range(i, N):                  # 끝의 값까지 조회하여
            if coin_li[j] > max_count:         # 더 큰 값이 있으면
                max_count = coin_li[j]         # 큰 값을 최신화하고
        
        if max_count > 0:                      # 큰 값이 있었으면
            answer += max_count - coin_li[i]   # 가격 차이를 정답에 더해준다.
     
    print('#' + str(test_case), answer)



# 뒤에서부터 시작하여 현재 최대 값으로 기준값을 잡고
# 기준 값과 현재 인덱스의 값과 비교하여 
# 현재 값이 최댓 값보다 크거나 같다면 최댓 값을 업데이트하고
# 현재 값이 최댓 값보다 작다면 정답에 최댓 값 - 현재 값의 가격 차이를 더한다. (현재 값에 구매해서 최댓값에 판다)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    coin_li = list(map(int, input().split()))
    answer = 0
    max_count = 0                       # 현재 판매가격(최댓값)

    for i in reversed(coin_li):         # 배열 거꾸로 순회
        if i >= max_count:              # 현재 값이 최댓값보다 크거나 같다면
            max_count = i               # 최댓값 업데이트
        else:                           # 현재 값이 최댓값보다 작다면
            answer += max_count - i     # 정답 값에 가격 차이를 더한다. (현재 값에 구매해서 최댓값에 판다)

    print('#' + str(test_case), answer)