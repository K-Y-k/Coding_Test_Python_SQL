# 미로문제는 BFS로 풀어야한다.
# 미로의 칸 이동된 값은 이동하기 전 위치 값에 +1

from collections import deque
import sys

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))         # valueError가 발생하므로 .rstrip()을 넣어야한다.


def bfs(x, y):
    dx = [-1,1,0,0]                                                     # 미로는 상하좌우만 이동된다하므로 
    dy = [0,0,-1,1]
    
    q = deque()                                                         # 큐 선언 및 큐에 현재 위치 값을 넣음
    q.append((x,y))                                                  
    
    while q:                                                            # 큐가 빌 때까지
        x, y = q.popleft();                                             # 큐의 앞의 원소 x,y값을 꺼내와서
        
        for i in range(4):                                              # 상하좌우를 순서대로 이동하고
            nx = x + dx[i]
            ny = y + dy[i]
             
            if 0<=nx<n and 0<=ny<m:                                     # 주어진 미로 인덱스에서 벗어나지 않고
                if graph[nx][ny] == 1:                                  # 0은 지나갈 수 없다고 했으므로 1이면
                    graph[nx][ny] = graph[x][y] + 1                     # 이동하기 전 위치 값에 +1을 해주고 
                    q.append((nx,ny))                                   # 큐에 넣는다.
                    
    return graph[n-1][m-1]                                              # 모든 루프를 돌고 난 후의 최종 n, m의 위치일 때의 값을 반환하고
                                                                        # (0, 0)부터 시작했으므로 n-1, m-1이 우리가 구하고 싶은 값이다.

print(bfs(0, 0))                                                        # (0, 0)부터 BFS가 시작되고 최종 반환된 (m, n)일 때의 값이 출력된다.