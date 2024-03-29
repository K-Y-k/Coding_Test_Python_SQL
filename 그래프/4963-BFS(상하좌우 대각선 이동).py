from collections import deque
import sys

dx = [-1,1,0,0, -1,1,-1,1]                             # 상하좌우 대각선까지 이동 좌표 선언
dy = [0,0,-1,1, -1,-1,1,1] 

def bfs(x, y):                                         # BFS 함수
    graph[x][y] = 0                                    # 현재위치를 섬으로 탐색했으므로 0으로 변경해서 탐색 대상에 제외한다.
    
    q = deque()                                        # 큐 선언 및 현재 좌표 값 넣기
    q.append((x, y))
    
    while q:                                           # 큐가 빌 때까지 반복
        x, y = q.popleft()                             # 큐의 제일 앞 원소의 x, y를 꺼내고
        
        for i in range(8):                             # 상하좌우 대각선 위치의 경우를 모두 구한다.
            nx = x + dx[i]
            ny = y + dy[i]
             
            if 0 <= nx < h and 0 <= ny < w:            # 해당 좌표가 주어진 인덱스에 벗어나지 않고
                if graph[nx][ny] == 1:                 # 해당 위치의 값이 1일 때
                    graph[nx][ny] = 0                  # 0으로 바꾸어 탐색대상에 제외되게 하고 
                    q.append((nx, ny))                 # 큐에 넣는다.


while True:
    w, h = map(int, sys.stdin.readline().split())       # 너비 높이 입력
     
    if w == 0 and h == 0:                               # 너비 높이가 0이면 반복 종료
        break
    else:                                               # 너비 높이가 주어진 경우
        graph = []                                            
        for _ in range(h):                              # 높이 만큼의 그래프 모델링을 하고
            graph.append(list(map(int, sys.stdin.readline().split())))
        
        count = 0                                       # 개수의 초기값을 0으로 초기화하고
        for i in range(h):                              # 높이 너비 2차원 반복으로 모두 조회하여
            for j in range(w):
                if graph[i][j] == 1:                    # 현재 위치가 1이면 섬이 있는 것이므로
                    count += 1                          # 섬의 개수를 카운팅하고 bfs를 진행한다.
                    bfs(i, j) 
                    
        print(count)                                    # 모든 루프로 탐색을 완료한 최종 섬의 총 개수 출력
            