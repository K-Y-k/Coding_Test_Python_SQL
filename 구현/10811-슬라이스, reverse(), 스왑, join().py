# i~j까지의 위치를 거꾸로 바꿔야하므로 슬라이스를 활용한 값을 reverse()로 뒤집고 저장한다.
# i~j의 슬라이스 값을 저장한 값으로 변경한다.


import sys

N, M = map(int, input().split())

num_li = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    temp = num_li[i-1:j]                            # i~j까지의 위치를 거꾸로 바꿔야하므로 슬라이스를 활용한 값을
    temp.reverse()                                  # 슬라이스를 활용한 값을 reverse()로 뒤집고 저장한다.
    num_li[i-1:j] = temp                            # i~j의 슬라이스 값을 저장한 값으로 변경한다.

print(' '.join(map(str, num_li)))