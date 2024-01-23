# 내가 푼 방식 = 순열
# 입력한 리스트에서 3개씩 뽑는 모든 경우의 수를 조회하여
# 해당 조건이 맞으면 정답 후보 리스트에 넣고
# 정답 후보 리스트의 최대값이 정답

from itertools import combinations

N, M = map(int, input().split())
blackJack_li = list(map(int, input().split()))
sum_li = []

c_blackJack = combinations(blackJack_li, 3)

for i in c_blackJack:
    total = sum(i)

    if total <= M:
        sum_li.append(total)


print(max(sum_li))



# 모든 루프를 순회하는 브루트포스 방식

N, M = map(int, input().split())
blackJack_li = list(map(int, input().split()))
sum_li = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = blackJack_li[i] + blackJack_li[j] + blackJack_li[k]

            if total <= M:
                sum_li.append(total)

print(max(sum_li))