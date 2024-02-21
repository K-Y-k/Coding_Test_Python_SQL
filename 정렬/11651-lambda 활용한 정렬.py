# y좌표가 우선순위로 증가하는 순서로 적용하고
# y좌표가 같을 때 x좌표가 증가하는 순서라고 했으므로
# 람다로 위 순서로 정렬을 적용한다.

import sys

N = int(input())

xy_list = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    
    xy_list.append([x, y])
    
# xy_list.sort(key=lambda x:(x[1], x[0]))
xy_list = sorted(xy_list, key=lambda x:(x[1], x[0]))   # 람다로 y값, x값 순으로 정렬을 적용한다.

for i in xy_list:
    print(i[0], i[1])