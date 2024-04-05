# 처음에는 총총이만 댄스를 추고 있다고 했으므로 
# 딕셔너리에 총총이만 초기화 해두고 

# 입력된 두 사람중 총총이 댄스를 추고 있는 사람이 있고 다른 사람은 춤을 아직 안춘 상황이라면
# 총총이 댄스 딕셔너리에 아직 추지 않은 사람을 추가하여 총총이 댄스를 추게 한다.
# 이 과정을 모두 반복한 후 총총이 댄스를 추고 있는 사람의 수가 문제에서 원하는 답이다.

import sys

N = int(sys.stdin.readline())

dance_dic = {'ChongChong': 1}
answer = 0

for _ in range(N):
    A, B = map(str, sys.stdin.readline().rstrip().split())

    if A in dance_dic and B not in dance_dic:
        dance_dic[B] = 1

    if B in dance_dic and A not in dance_dic:
        dance_dic[A] = 1


answer = len(dance_dic)

print(answer)



# set 활용 방식

import sys

N = int(sys.stdin.readline())

dance_set = {'ChongChong'}
answer = 0

for _ in range(N):
    A, B = map(str, sys.stdin.readline().rstrip().split())

    if A in dance_set:
        dance_set.add(B)

    if B in dance_set:
        dance_set.add(A)


answer = len(dance_set)

print(answer)