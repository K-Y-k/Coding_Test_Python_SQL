import sys
from collections import deque

N = int(input())

q = deque()

for _ in range(N):
    command = list(sys.stdin.readline().split()) # 여러번 입력받을 때는 sys.stdin.readline()이 빠르다.

    if command[0] == 'push':
        q.append(int(command[1]))                # 삽입
    elif command[0] == 'pop':
        if q:
            print(q.popleft())                   # 제일 앞 원소 제거
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))                            # 큐 길이
    elif command[0] == 'empty':
        if q:                                    # 큐 빈 여부
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if q:
            print(q[0])                          # 큐의 제일 앞 원소 확인
        else:
            print(-1)
    elif command[0] == 'back':
        if q:
            print(q[-1])                         # 큐의 제일 뒤 원소 확인
        else:
            print(-1)
