# DFS로 탐색하면서 사이클이 있는지 확인한다. 
# 문제에서 사이클의 여부는 선분의 길이가 최소선분 길이인 4이상이면서 시작좌표와 끝좌표가 같으면 사이클이 있다고 한다.


N, M = map(int,input().split())                                      # 너비, 높이입력

graph = []                                                           # 입력 값에 따른 그래프 모델링 해당 입력 값이 색상으로 간주 
for _ in range(N):
    graph.append(list(input()))
    
visited = [[False]*M for _ in range(N)]                               # 방문여부 False로 초기화 
dx = [-1,1,0,0]                                                       # 상(-1,0), 하(1,0), 좌(0,-1), 우(0,1) 선언
dy = [0,0,-1,1]
cycle = False                                                         # 사이클 여부 False로 초기화  

def dfs(x, y, depth, color, start_x, start_y):                        # dfs 깊이 탐색 (주어진 x,y좌표, 현재 깊이, 색상, 시작위치의 x,y좌표)
    global cycle

    for i in range(4):                                                # 상하좌우로 이동하여 확인
        nx = x + dx[i]
        ny = y + dy[i]
        
        if cycle is True:                                             # 사이클을 하나 찾으면 종료시키기
            return
        
        if 0<=nx<N and 0<=ny<M:                                       # 주어진 인덱스 범위를 벗어나지 않고
            if depth>=4 and nx==start_x and ny==start_y:              # CASE1: 깊이가 4이면서 현재 이동된 x,y 좌표가 처음 시작했던 x,y좌표와 같다면
                cycle=True                                            #        사이클을 발견한 것이므로 True로 반환하여 종료시키기
                return

            if visited[nx][ny]==False and graph[nx][ny]==color:       # CASE2: 방문하지 않았고 이동된 좌표의 값(=색상)이 이전 위치의 값(색상)과 같다면
                visited[nx][ny] = True                                #        방문처리를 한 후
                dfs(nx, ny, depth+1, color, start_x, start_y)         #        다음 깊이의 DFS를 진행하고
                visited[nx][ny] = False                               #        백트랙킹을 해야하므로 다시 False로 바꿔줘야함


for i in range(N):                                                    # 처음부터 끝까지의 좌표를 조회하면서
    for j in range(M):
        visited[i][j] = True                                          # 방문처리를 하고
        
        start_x = i                                                   # 시작위치의 x,y좌표를 저장하고
        start_y = j
        
        dfs(i, j, 1, graph[i][j], start_x, start_y)                   # DFS를 진행한다.
        
        if cycle:                                                     # 해당 위치의 DFS가 진행된 후 사이클이 있으면 
            print('Yes')                                              # Yes를 출력하고 종료
            exit()
            
print('No')                                                           # 모든 루프를 다 돌아도 사이클을 못찾았으면 No출력
