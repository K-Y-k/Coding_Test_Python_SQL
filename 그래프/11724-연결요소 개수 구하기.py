import sys
sys.setrecursionlimit(10 ** 6)                           # 만약 재귀를 사용해서 풀어야 하는 문제라면 선택이 아닌 필수

N, M = map(int, input().split())                         # 정점, 간선 개수 입력

edge = [[] for _ in range(N+1)]                          # 인접리스트 방식의 간선 선언
visited = [False] * (N+1)                                # 방문 리스트 선언

for _ in range(M):                                       # 간선 개수만큼 반복해서 입력한 값을 간선에 넣기
    u, v = map(int, sys.stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)
    
connected = 0                                            # 연결요소 개수 초기화

def dfs(idx):                                            # dfs 함수 현재 위치의 정점과 이 정점과 연결된 다른 정점을 깊이 탐색 진행
    global visited
    visited[idx] = True
    
    for i in edge[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            
for i in range(1, N+1):                                  # 각 노드를 순서대로 진행하여 
    if not visited[i]:                                   # 새로운 방문지점이 있으면 새로 시작하는 정점이므로 연결요소가 따로 있다는 뜻이므로
        connected += 1                                   # 연결요소 개수를 증가시키고 DFS진행
        dfs(i)

print(connected)                                         # 연결요소 개수 출력