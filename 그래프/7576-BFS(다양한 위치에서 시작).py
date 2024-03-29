# 이 문제는 '최소일수', '주변의 토마토를 익힘'이라는 뜻을 보아 
# DFS처럼의 깊이 탐색이 아닌 BFS 너비우선 탐색으로 해야한다.


from collections import deque
import sys

M, N = map(int, input().split())                                    # 토마토 농장의 너비, 높이 입력

graph = []                                                          # 토마토의 입력 값을 통한 그래프 모델링
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
dx = [-1, 1, 0, 0]                                                  # 상하좌우 
dy = [0, 0, -1, 1]


q = deque()                                                         # 큐 선언 및 토마토가 1의 주변으로 부터 상하좌우로 퍼져나가기 시작하므로
for i in range(N):                                                  # 1인 것은 큐에 넣는다.
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))    

def bfs():
    while q:                                                        # 큐가 빌 때까지
        x, y = q.popleft()                                          # x, y를 꺼내고
        
        for i in range(4):                                          # 상(-1,0), 하(1,0), 좌(0,-1), 우(0,1)
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M:                                 # 이동한 위치중 주어진 토마토 농장의 인덱스를 벗어나지 않고
                if graph[nx][ny] == 0:                              # 그 위치의 값이 0인 것은 이전 위치의 값 +1을 한 후 큐에 넣는다.
                    graph[nx][ny] = graph[x][y] + 1                 # 이전 위치의 값 +1을 한 후
                    q.append((nx, ny))                              # 큐에 넣는다.
            
bfs()                                                               # 순차적으로 1인 것을 큐에 넣었던 것부터 상하좌우로 BFS를 모두 진행

result = 0
for i in range(N):                                                  # BFS로 모든 진행을 마친 그래프를 다시 조회해서
    for j in range(M):              
        if graph[i][j] == 0:                                        # 0인 값이 아직도 있으면 -1을 출력하고 프로그램 종료
            print(-1)
            exit()
    result = max(result, max(graph[i]))                             # 0인 값이 없으면 현재 i위치의 행 중 제일 큰 값을 넣어 모두 순회하므로 결국 제일 큰 값이 저장될 것이다.

print(result - 1)                                                   # 토마토가 모두 익는 최소 일수를 출력한다. (0의 위치부터 시작했으므로 -1을 한 것)