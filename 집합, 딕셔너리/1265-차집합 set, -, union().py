# 내가 푼 방식 - 시간 초과
# 각 A와 B집합을 for문으로 조회하여 포함되지 않은 것을 차집합으로 간주한 후 합쳤지만 시간초과

N, M = map(int, input().split())

A_li = list(map(int, input().split()))
B_li = list(map(int, input().split()))

AB_li = []
BA_li = []


for i in A_li:                                # 각 A와 B집합을 for문으로 조회하여 포함되지 않은 것을 차집합으로 간주한 후
    if i not in B_li:
        AB_li.append(i)

for i in B_li:
    if i not in A_li:
        BA_li.append(i)


answer_li = AB_li + BA_li                     # 합쳤지만 시간초과

print(len(answer_li))



# 각 set인 A B를 
# -로 차집합을 구한 후
# union함수로 합칠 수 있었다.

N, M = map(int, input().split())

A_set = set(map(int, input().split()))       # 각 set인 A B를 
B_set = set(map(int, input().split()))

AB_set = A_set - B_set                       # -로 차집합을 구한 후
BA_set = B_set - A_set

answer_li = AB_set.union(BA_set)             # union함수로 합칠 수 있었다.

print(len(answer_li))