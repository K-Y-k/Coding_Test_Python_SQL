# 내가 푼 방식 - 모든 구간을 조회하며 합하기 = 시간초과
# 연속합의 K범위가 N까지 올 수 있는데 N의 최대값이 10만까지라 했으므로
# 이 범위까지  원소를 일일이 훑으며 더해주는 sum함수로 적용하면 시간 복잡도가 O(N2)에 가깝게 되므로 성능이 매우 좋지 않다.

N, K = map(int, input().split())

temperature_li = list(map(int, input().split()))
prefix_li = []


for i in range(len(temperature_li)-K):
    prefix_li.append(sum(temperature_li[i:i+K]))


print(max(prefix_li))



# 여러번 사용될 만한 정보는 미리 구해서 저장해 놓을수록 유리하다.
# 따라서 입력 받은 배열을 누적 합 배열에 따로 저장해두고,
# 구하려 하는 구간 a, b에 해당하는 두 원소의 차를 구해서 그 구간의 합을 구하는 방식을 사용한다.
# P[right] - P[left-1]을 수행하면 시간 복잡도는 O(1)이 된다.

N, K = map(int, input().split())

temperature_li = list(map(int, input().split()))
prefix_li = [sum(temperature_li[:K])]                                         # 누적합 배열 초기화


for i in range(len(temperature_li)-K):
    prefix_li.append(prefix_li[-1] + temperature_li[i+K] - temperature_li[i]) # 처음부터 조회하면 이전 누적합의 첫위치가 현재위치이므로 이전 누적합에서 현재 위치의 값을 빼고 K앞의 값을 더하면 된다.


print(max(prefix_li))