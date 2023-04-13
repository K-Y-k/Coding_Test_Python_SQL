from collections import deque       
import sys

N = int(input())

graph = []                                                                 # 그래프 모델링을 할 인접 리스트
count_list = []                                                            # 최종 개수를 넣어줄 리스트

for _ in range(N):                                                         # 입력한 값 만큼
    graph.append(list(map(int, sys.stdin.readline().rstrip())))            # 여기서는 무조건 .rstrip()으로 오른쪽 공백을 제거해야한다.
    
def bfs(x, y):
    dx = [-1, 1, 0, 0]                                                     # 상(-1,0), 하(1,0), 좌(0,-1), 우(0,1)
    dy = [0, 0, -1, 1]
    
    q = deque()             
    q.append((x, y))
    
    graph[x][y] = 0                                                        # 현재 위치의 값을 0으로 바꿔 다음 검색 대상이 되지 않게 한다.
    count = 1                                                              # 첫 카운트 값을 1로 초기화
    
    while q:                                                               # 큐가 빌 때까지
        x, y = q.popleft()                                                 # 앞의 원소(x,y)를 꺼내오고
        
        for i in range(4):                                                 # 현재 위치에서 상, 하, 좌, 우로 이동해서 
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:         # 인덱스를 벗어나지 않고 해당 인덱스의 원소값이 1이면
                graph[nx][ny] = 0                                          # 위치는 발견한 것이므로 검색조건이 되지 않게 0으로 바꿔주고
                q.append((nx, ny))                                         # 큐에 넣어주고
                count += 1                                                 # 개수를 증가시킨다.
                
    count_list.append(count)                                               # 루프를 모두 돌린 후의 최종 개수를 카운트 리스트에 넣어준다.
    
for i in range(N):                                                         # 행렬 형태이므로 2차원 배열로 처음부터 루프를 돌려 
    for j in range(N):
        if graph[i][j] == 1:                                               # 현재 위치 값이 1이면  
            bfs(i, j)                                                      # BFS를 진행한다.
            
count_list.sort()                                                          # 문제에서 오름차순으로 구하라고 했으므로 오름차순 정렬
print(len(count_list))                                                     # 카운트 리스트의 길이로 각 종류의 개수 출력
for i in count_list:                                                       # 각 개수 출력
    print(i)