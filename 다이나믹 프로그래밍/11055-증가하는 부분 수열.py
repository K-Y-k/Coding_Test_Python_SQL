N = int(input())

A_list = list(map(int, input().split()))

d = A_list[:]                                   # dp를 위에 입력한 수열 값으로 똑같이 만든다. 아래에서 비교처리를 위해

for i in range(1, N):
    for j in range(i):
        if A_list[j] < A_list[i]:               # 증가하는 수열인 경우 위에 i번째 위치에 넣어둔 수열 값과 비교해서 큰 값을 넣는다.
            d[i] = max(d[i], d[j]+A_list[i])  
                                                # 위 경우가 아니면 기존에 넣어둔 값을 최대 값으로 유지 
        
print(max(d))
