# 내가 시도한 방식 : count 잘못된 카운팅
# bfs로 탐색하면서 벽이 아니면 카운팅처리하며 최종 끝 좌표에 도착할 경우 카운트한 것을 리스트에 담아 
# 최종 카운트 리스트의 최솟값을 반환하려했지만 카운트하는 방식이 잘못됨

from collections import deque

def solution(maps):
    answer = 0
    count_list = []
    n = len(maps[0])
    m = len(maps)
    visited = [[False] * n for i in range(m)]
    visited[0][0] = True

    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        nonlocal count_list
        
        q = deque()
        q.append((x,y))
        count = 0
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<m and 0<=ny<n:
                    if visited[nx][ny] == False and maps[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        count += 1
                
                if (nx,ny) == (m,n):
                    count_list.append(count)
                    count = 0

    bfs(0, 0)

    if len(count_list) == 0:
        answer = -1
    else:
        answer = min(count_list)

    return answer



# 그래서 개선한 방안 : visited에 거리 적용해가며 탐색하기
# 내가 부족했던 점 n * m의 행 열 기준을 정확히 인지하지 못하여 행 열 인덱스 위치 잘못 적용해 나감

from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)                                             # 행
    m = len(maps[0])                                          # 열

    visited = [[0] * m for _ in range(n)]                     # 0의 초깃값으로 생성 / n을 행, m을 열로 선언했으므로 조심
    visited[0][0] = 1                                         # 문제에서 시작 좌표부터 카운팅했으므로 1적용
    
    dx = [-1, 1, 0, 0]                                        # 행 좌표
    dy = [0, 0, -1, 1]                                        # 열 좌표
    
    def bfs(x, y):
        q = deque()
        q.append((x,y))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<n and 0<=ny<m:                           
                    if visited[nx][ny] == 0 and maps[nx][ny] == 1: # 아직 방문하지 않았고 벽이 아니면
                        visited[nx][ny] = visited[x][y] + 1        # 이전 위치의 거리에서 +1 적용해 나간다.
                        q.append((nx, ny))
                
    bfs(0, 0)
    
    if visited[n-1][m-1] == 0:                                    
        answer = -1
    else:
        answer = visited[n-1][m-1]
        
    return answer