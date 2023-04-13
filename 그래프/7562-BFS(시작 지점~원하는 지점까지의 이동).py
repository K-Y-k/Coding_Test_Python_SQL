from collections import deque
import sys

T = int(input())

dx = [-2,-1, 1, 2,  2, 1,-1,-2]                                      # 문제에서 주어지는 칸을 잘 확인하고 정확하게 넣기
dy = [1,  2,  2, 1,-1,-2,-2,-1]

def bfs(x, y):                                                       # BFS 함수
    q = deque()                                                      # 큐 선언 및 시작 위치를 넣는다.
    q.append((x, y))
    
    while q:                                                         # 큐가 빌 때까지 반복
        x, y = q.popleft()                                           # 큐에서 제일 앞 원소의 x, y를 꺼낸다.
        if x == end_x and y == end_y:                                # 만약 원하는 위치의 x,y를 꺼냈으면 그 위치의 값을 리턴한다.
            return graph[x][y]
        
        for i in range(8):                                           # 나이트의 이동가능한 거리들 모두 이동해본다.
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<rowCol and 0<=ny<rowCol:                        # 주어진 체스판의 인덱스가 벗어나지 않고
                if graph[nx][ny] == 0:                               # 이동한 위치가 0이면 아직 방문하지 않은 것이므로
                    graph[nx][ny] = graph[x][y] + 1                  # 이동하기 전의 위치 값에 + 1로 최신화해주고
                    q.append((nx, ny))                               # 큐에 넣어준다.
                

for _ in range(T):                                                   # 테스트 케이스 입력 값 만큼 반복
    rowCol = int(input())                                            # 체스판 길이 입력
    
    graph = []                                                       # 체스판 길이 만큼 0으로 그래프 모델링
    for _ in range(rowCol):
        graph.append([0]*rowCol)
    
    start_x, start_y = map(int, input().split())                     # 시작지점 입력
    end_x, end_y = map(int, input().split())                         # 원하는 지점 입력
    
    print(bfs(start_x, start_y))                                     # 시작지점부터 BFS를 진행하여 원하는 지점의 값의 이동 값 출력