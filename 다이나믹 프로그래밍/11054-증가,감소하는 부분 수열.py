# 바이토닉 부분 수열
# : 특정 수를 기준으로 왼쪽에 위치한 숫자는 증가하고 오른쪽에 위치한 숫자는 감소하는 형태를 띤 부분 수열을 의미


N = int(input())

num_list = list(map(int, input().split()))

increase = [1] * N                                              # 증가하는 부분 dp 초기값은 [0]일 때 1이 최대 값이므로 1로 초기화 해둠
decrease = [1] * N                                              # 감소하는 부분 dp 초기값은 [0]일 때 1이 최대 값이므로 1로 초기화 해둠
 

for i in range(N):                                              # 증가하는 부분의 수열 처리
    for j in range(i):
        if num_list[j] < num_list[i]:
            increase[i] = max(increase[i], increase[j]+1)

for i in reversed(range(N)):                                    # 감소하는 부분의 수열 처리는 인덱스를 역으로 뒤집어서 진행해야한다.
    for j in reversed(range(i, N)):                             # 뒤집어서 해야진행하므로 (N-1)~i번째의 인덱스를 비교해나간다.
        if num_list[j] < num_list[i]:
            decrease[i] = max(decrease[i], decrease[j]+1)
            
result = [0] * N

for i in range(N):
    result[i] = increase[i] + decrease[i]-1                     # 증가, 감소의 기준 값이 2번 들어가있으므로 1을 빼준 것이다.

print(max(result))