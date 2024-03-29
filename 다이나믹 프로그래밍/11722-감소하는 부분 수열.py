N = int(input())

num_list = list(map(int, input().split()))

d = [1] * N                                     # d[0]일 때 감소하는 부분중 가장 긴 길이는 1이므로 1로 초기화 해야한다.

for i in range(N):
    for j in range(i):
        if num_list[j] > num_list[i]:           # 감소하는 부분이므로 j위치의 값이 i위치의 값보다 커야한다.
            d[i] = max(d[i], d[j]+1)            # 기존 d[i]와 d[j]+1과 비교해서 더 긴 길이를 넣는다. 

print(max(d))                                   # 각 위치의 가장 긴 길이들 중 최대 값을 출력한다.