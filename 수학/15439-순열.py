# 상의, 하의가 각 N개의 색상으로 구비하고 있고
# 상의 하의를 같이 입은 세트로 비교하는데
# 상,하의가 모두 다른 색상인 경우만 구하고 싶으므로

# N개의 색상 종류별로 하나씩 있는 리스트에서 순열로 구하면 서로 다른 색상의 조합이 된다.

from itertools import permutations

N = int(input())
answer = 0

shirtAndPants_li = [i for i in range(N)]
p = permutations(shirtAndPants_li, 2)


for a, b in p:
    if a != b:
        answer += 1

print(answer)