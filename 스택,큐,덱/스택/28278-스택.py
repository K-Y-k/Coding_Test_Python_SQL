# 명령어와 삽일할 때의 정수를 받아올 때가 있으므로 리스트로 받아왔고
# 각 명령어에 따른 동작을 구현했다. 
# 시간초과 발생한 이유가 일반 input()이 아닌 sys.stdin.readline으로 활용해야했다.

import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
