# 처음에는 기존에 풀었던 상하좌우 방식을 이용해서
# 큐에 추가할 때마다 벽을 부쉈는지 여부에 따른 count로 갱신해가며 최종 벽을 부순 count가 답일 줄 알았다.

# 하지만 문제에 최소한으로 벽을 부수며 갈 수 있는 최종 벽을 부순 count를 원하여 다른 방식으로 접근해야함
# 즉, 빈방인 경우 우선순위를 앞에 두어서(=appendleft()활용) 해당 방으로 먼저 이동하게 만들어야한다.



# 내가 생각한 count를 매개변수로 갱신하며 반환 + 우선순위 적용한 BFS
from collections import deque
import sys

M, N = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False]*M for _ in range(N)]
count = 0

def bfs():
    q = deque()
    q.append((0,0,0))
    
    while q:
        x, y, count = q.popleft()                                 # x, y, 현재까지 벽을 부순 횟수를 꺼내와서
        
        if x == (N-1) and y == (M-1):                             # 끝까지 이동했을 때 최종 벽을 부순 횟수를 반환
            return count
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and graph[nx][ny] == 0:    # 방문하지 않았고 0이면
                    visited[nx][ny]=True                          # 방문처리를 해주고
                    q.appendleft((nx, ny, count))                 # 빈방이므로 최소한으로 부숴야하므로 우선순위를 제일 앞에 넣었다. (현재 위치와 기존 부순 횟수로 넣음)

                elif not visited[nx][ny] and graph[nx][ny] == 1:  # 방문하지 않았고 1이면
                    visited[nx][ny]=True                          # 방문처리를 해주고
                    q.append((nx, ny, count+1))                   # 현재 위치와 1은 벽을 부숴야하므로 벽을 부순 횟수에 +1을 해주고 벽을 부쉈으므로 우선순위 없이 큐 뒤에 넣는다.
                    
print(bfs())                                                      # 반환된 최종 벽을 부순 횟수 출력됨




# 가중치를 활용하여 최단경로를 구하는 다익스트라 알고리즘을 적용한 BFS
from collections import deque
import sys

M, N = map(int, input().split())                                            # 가로 M, 세로 N

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]   # 그래프 모델링

dist = [[-1] * M for _ in range(N)]                                         # 가중치 부여를 위한 리스트 선언

dx = [-1,1,0,0]                                                             # 상하좌우 선언
dy = [0,0,-1,1]

def bfs():                                                                  
    q = deque()                                                             # 큐 선언 및 초기 값 넣기
    q.append((0,0))
    dist[0][0] = 0                                                          
    
    while q:                                                                
        x, y = q.popleft()                                                  # 제일 앞의 x,y를 꺼내와서
        
        for i in range(4):                                                  # 각 상하좌우 이동시 조회
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M:                                         # 가로 세로의 인덱스가 벗어나지 않고
                if dist[nx][ny] == -1 and graph[nx][ny] == 0:               # 가중치가 아직 적용되지 않았고 벽이 없는 빈방인 경우
                    dist[nx][ny] = dist[x][y]                               # 기존 가중치를 적용하고
                    q.appendleft((nx, ny))                                  # 벽을 최소한으로 부수는 것이므로 우선순위를 큐 제일 앞(appendleft())에 넣는다.
                    
                elif dist[nx][ny] == -1 and graph[nx][ny] == 1:             # 가중치가 아직 적용되지 않았고 벽이 있는 경우는
                    dist[nx][ny] = dist[x][y] + 1                           # 기존 가중치에 +1을 해서 벽을 부순 횟수를 갱신 
                    q.append((nx, ny))                                      # 벽을 부순 경우이므로 우선순위 없이 큐 뒤에 넣는다.
                        
bfs()                                                                       # BFS함수를 진행하면서 가중치가 모두 적용되고
print(dist[N-1][M-1])                                                       # 문제에서는 (1,1)부터 시작했는데 내가 구현한 코드는 (0,0)부터 시작했으므로 (M-1, N-1)의 가중치를 출력해야한다.