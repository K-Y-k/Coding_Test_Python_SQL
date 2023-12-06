# 상, 하, 좌, 우 이동을 위한 좌표 생성과
# 
# 방문하지 않았고 X일 때는 



from collections import deque

def solution(maps):
    answer = []
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * (m+1) for _ in range(n+1)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    
    def bfs(x, i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = True
        
        area = int(maps[i][j])
        
        while q:
            x, y = q.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X': # X가 아니고 방문하지 않았고 숫자가 있으면
                    visited[nx][ny] = True                                                      # 방문처리
                    area += int(maps[nx][ny])                                                   # 현재 위치의 섬의 값을 추가
                    q.append((nx, ny))                                                          # 큐에 넣기
                    
        answer.append(area)
            
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:           # X가 아니고 숫자가 있으면 BFS 진행
                bfs(maps[i][j], i, j)
    
    
    if len(answer) > 0:                                           # 정답에 섬을 측정한 값이 있으면
        answer.sort()                                             # 오름차순으로 정렬하고 반환
        return answer
    else:                                                         # 없으면 [-1]로 반환
        return [-1]