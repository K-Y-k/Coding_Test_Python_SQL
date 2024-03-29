# 트리의 탐색은 DFS/BFS 모두 가능하다.

from collections import deque
import sys

N = int(input())

visited = [False] * (N+1)                                             # 방문 여부 초기화

graph = [[] for _ in range(N+1)]                                      # 그래프 모델링
for i in range(N-1):                                                  # 간선의 개수가 N-1이므로 N-1까지 반복
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph[N].append(M)
    graph[M].append(N)
    

def bfs():
    q = deque()                                                       # 큐 선언 및 초기 값은 문제에서 주어진 루트 1 삽입
    q.append(1)
    
    while q:                                                          # 큐가 빌 때까지 반복
        idx = q.popleft()                                             # 앞의 원소 가져오고
        
        for i in graph[idx]:                                          # 해당 원소에 연결된 정점을 조회하여
            if not visited[i]:                                        # 방문하지 않았으면
                visited[i] = idx                                      # 방문 값을 방문하지 않은 원소 값을 넣고
                q.append(i)                                           # 큐에 넣기
                
bfs()                                                                 # BFS 시작

result = visited[2:]                                                  # 2번노드부터 순서대로 출력하기 위해 2번째 원소부터 넣고 
for i in result:                                                      # 차례로 출력
    print(i)

