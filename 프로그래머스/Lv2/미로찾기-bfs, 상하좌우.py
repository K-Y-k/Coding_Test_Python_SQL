# 시작지점에서 레버위치까지의 이동과
# 레버위치에서 끝지점까지의 이동을 각자 구한 후
# 이 둘의 거리를 더한다.

# 주의점은 
# 1. 각 두 거리를 측정할 때 방문여부를 초기화한 후 시작해야한다.
# 2. 또한 거리를 따로 선언하여 넣는 것이 아닌 좌표를 넣는 과정에서 같이 넣어서 진행해야한다.

from collections import deque

def solution(maps):
    n = len(maps)                                        # 행
    m = len(maps[0])                                     # 열
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] =='S':                         # 시작위치의 좌표
                s_x = i
                s_y = j
            if maps[i][j] == 'L':                        # 레버위치의 좌표
                l_x = i
                l_y = j
    
    
    def bfs(x, y, end):
        visited = [[False] * (m+1) for _ in range(n+1)]   # 주의점1. 각 두 거리를 측정할 때 방문여부를 초기화한 후 시작해야한다.
        
        q = deque() 
        q.append((x, y, 0))                               # 주의점2. 또한 거리를 따로 선언하여 넣는 것이 아닌 좌표를 넣는 과정에서 같이 넣어서 진행해야한다.
        visited[x][y] = True
        
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        while q:
            x, y, distance = q.popleft()
            
            if maps[x][y] == end:                          # 목표 위치까지 도착했으면
                return distance                            # 거리 반환
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] !='X':
                    visited[nx][ny] = True
                    q.append((nx, ny, distance+1))
                    
        return -1                                          # 모든 큐를 진행했어도 도착하지 못했으면 막혔다는 뜻이므로 -1 반환
    

    path1 = bfs(s_x, s_y, 'L')                             # 시작위치~레버위치까지 거리 탐색
    path2 = bfs(l_x, l_y, 'E')                             # 레버위치~끝위치까지의 거리 탐색
    
    if path1 != -1 and path2 != -1:
        answer = path1 + path2
    else:
        answer = -1
    
    return answer