from collections import deque       # 덱 라이브러리

import sys

N = int(input())

deque = deque()

for _ in range(N):
    a = sys.stdin.readline().split()
    
    if a[0] == 'push_front':
        deque.appendleft(a[1])      # 덱은 appendleft로 앞에 값을 넣을 수 있다.
    elif a[0] == 'push_back':
        deque.append(a[1])
    elif a[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())   # 덱은 popleft로 앞의 값을 뺄 수 있다.
    elif a[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif a[0] == 'size':
        print(len(deque))
    elif a[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif a[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
     