# 덱의 사용법을 묻는 문제이다
# 덱은 앞뒤 양쪽에서 값을 넣고 뺄 수 있는 자료구조이다.
# 앞에 값을 넣는 연산 = appendleft()
# 앞에 값을 빼는 연산 = popleft()
# 뒤에 값을 넣는 연산 = append()
# 뒤에 값을 빼는 연산 = pop()

import sys
from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        q.appendleft(command[1])
    elif command[0] == 2:
        q.append(command[1])
    elif command[0] == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == 4:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif command[0] == 5:
        print(len(q))
    elif command[0] == 6:
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 8:
        if q:
            print(q[-1])
        else:
            print(-1)