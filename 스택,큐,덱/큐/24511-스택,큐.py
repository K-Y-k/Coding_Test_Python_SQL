# 내가 푼 방식 - 시간 초과
# 데이터 구조에 따라 큐와 스택을 리스트에 담아준 후
# 삽입하는 값일 일일히 각 데이터 구조에 따른 문제에서의 로직을 적용시켜주었으나
# 이중 for문으로 시간 초과가 발생하였다..

from collections import deque

N = int(input())

structure = list(map(int, input().split()))
num_li = deque(list(map(int, input().split())))
data_structure = []

for idx, val in enumerate(structure):
    if val == 0:
        data_structure.append(deque([num_li[idx]]))
    else:
        data_structure.append([num_li[idx]])


M = int(input())
add_li = list(map(int, input().split()))
answer = []

for i in add_li:
    temp = data_structure[0]

    for idx, val in enumerate(data_structure):
        if idx == 0:
            if structure[idx] == 0:
                data_structure[idx].appendleft(i)
                temp = data_structure[idx].pop()
        else:
            if structure[idx] == 0:
                data_structure[idx].appendleft(temp)
                temp = data_structure[idx].pop()

    answer.append(temp)


print(' '.join(map(str, answer)))



# 주목할 점은
# 큐는 앞에 삽입하고 pop하므로 기존 값이 빠지고 새로운 값이 대입되고
# 스택은 뒤에 삽입하고 pop하므로 새로운 삽입하려는 값이 그대로 보존되어 의미가 없는 동작이 된다.

# 근데 우리는 값이 빼와진 리턴 값을 구해야하므로
# 현재 넣는 곳이 큐일 때만 리턴 리스트에 기존 값을 넣은후

# 처음 ~ 끝 작업순으로 넣었으므로 리턴 리스트가 거꾸로 되어
# 처음 작업할 때의 리턴한 값이 앞이 되도록 뒤집어준 후
# 큐가 아닌 경우는 스택은 새로 삽입하려던 값이 리턴되어야 하므로
# 리턴 리스트 뒤에 삽입하려던 값을 모두 넣어준 후
# 리턴 리스트 앞에서부터 삽입한 횟수만큼만 출력하면 리턴 값이 된다.

# 큐만 빼와지고 스택은 의미없는 동작까지는 알아챘으나
# 이를 응용한 효율적인 로직 생각이 어려웠다..

N = int(input())
structure = list(map(int, input().split()))
num_li = list(map(int, input().split()))

M = int(input())
add_li = list(map(int, input().split()))

return_li = []
answer = []

for i in range(N):
    if structure[i] == 0:                       # 현재 넣는 곳이 큐일 때만
        return_li.append(num_li[i])             # 리턴 리스트에 기존 값을 넣은후

return_li.reverse()                             # 처음 ~ 끝 작업순으로 넣었으므로 리턴 리스트가 거꾸로 되어
                                                # 처음 작업할 때의 리턴한 값이 앞이 되도록 뒤집어준 후

# 큐가 아닌 경우는 스택은 새로 삽입하려던 값이 리턴되어야 하므로
for i in range(M):
    return_li.append(add_li[i])                 # 리턴 리스트 뒤에 삽입하려던 값을 모두 넣어준 후
    answer.append(return_li[i])                 # 리턴 리스트 앞에서부터 삽입한 횟수만큼만 정답 리스트에 넣고

print(' '.join(map(str, answer)))               # 출력하면 리턴 값이 된다.