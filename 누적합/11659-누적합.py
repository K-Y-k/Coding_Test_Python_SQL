# 내가 푼 방식 - 모든 구간을 조회하며 합하기 = 시간초과
# 배열에서 구간의 합을 구할 때 배열과 구간의 크기가 모두 크다면,
# 배열의 구간에서 원소를 일일이 훑으며 더해주는 것은 시간 복잡도가 O(N2)에 가깝게 되므로 성능이 매우 좋지 않다.

import sys

N, M = map(int, sys.stdin.readline().split())

num_arr = list(map(int, sys.stdin.readline().split()))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    print(sum(num_arr[a-1:b]))



# 여러번 사용될 만한 정보는 미리 구해서 저장해 놓을수록 유리하다.
# 따라서 입력 받은 배열을 누적 합 배열에 따로 저장해두고,
# 구하려 하는 구간 a, b에 해당하는 두 원소의 차를 구해서 그 구간의 합을 구하는 방식을 사용한다.
# P[right] - P[left-1]을 수행하면 시간 복잡도는 O(1)이 된다.

import sys

N, M = map(int, sys.stdin.readline().split())

num_arr = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]                                         # 누적합 배열 초기화

for i in range(len(num_arr)):                            # 입력한 값들에 대한 누적합을 누적합 배열에 넣기
    prefix_sum.append(prefix_sum[-1] + num_arr[i])


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    print(prefix_sum[b] - prefix_sum[a-1])               # a, b 구간의 누적합 배열의 원소 값의 차로 그 구간의 합을 구한다.