# 배낭의 무게와 가치를 한쌍으로 리스트에 담고
# 담은 리스트의 무게와 가치가 들어있는 각 쌍을 조회하면서
# 해당 쌍에서의 K무게부터 현재 무게인 역순으로 가치의 최대값을 갱신해 나간다.

# 주의점은 K무게부터 현재 무게인 역순으로 해야한다.

import sys

N, K = map(int, input().split())

item_weight_li = []

for _ in range(N):                                  # 배낭의 무게와 가치를 한쌍으로 리스트에 담고
    w, v = map(int, sys.stdin.readline().split())
    item_weight_li.append((w, v))


dp = [0] * (K+1)                                    # 무게에 따른 최대값에 대한 dp 초기화

for i in range(N):                                  # 담은 리스트의 무게와 가치가 들어있는 각 쌍을 조회하면서
    weight = item_weight_li[i][0]
    value = item_weight_li[i][1]

    for j in range(K, weight-1, -1):                # 해당 쌍에서의 K무게부터 현재 무게인 역순으로 가치의 최대값을 갱신해 나간다.
        dp[j] = max(dp[j], dp[j-weight] + value)


print(dp[-1])
