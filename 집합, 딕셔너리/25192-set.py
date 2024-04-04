# 내가 푼 방식 - 시간 초과
# ENTER이후 들어가는 닉네임이 중복이 아니면 카운팅되므로 
# 리스트에 넣고 닉네임이 닉네임이 들어가 있는지 확인 후 카운팅했지만 시간초과

import sys

N = int(sys.stdin.readline())

gom_message_li = []
answer = 0

for _ in range(N):
    word = str(sys.stdin.readline().rstrip())

    if word == 'ENTER':
        gom_message_li.clear()
    else:
        if word not in gom_message_li:
            gom_message_li.append(word)
            answer += 1


print(answer)



# 리스트가 아닌 set 집합에 넣고 비교처리 하니 정상 작동

import sys

N = int(sys.stdin.readline())

gom_message_li = set()
answer = 0

for _ in range(N):
    word = str(sys.stdin.readline().rstrip())

    if word == 'ENTER':
        gom_message_li.clear()
    else:
        if word not in gom_message_li:
            gom_message_li.add(word)
            answer += 1


print(answer)