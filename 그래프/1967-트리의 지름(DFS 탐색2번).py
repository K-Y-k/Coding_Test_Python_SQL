# 트리에 존재하는 모든 경로 중에서 가장 긴 것의 길이를 트리의 지름이라고 한다.
# 트리의 지름은 DFS/BFS 탐색 2번으로 구할 수 있다.
# 1. 한 정점 s에서 시작하여 모든 정점까지의 거리를 구한다. 이 때, 가장 먼 거리인 정점을 u라고 한다.
# 2. u에서 시작하여 모든 정점까지의 거리를 구한다. 이 때, 가장 먼 거리인 정점 v를 구한다.
# 3. d(u, v)를 u와 v사이의 거리라고 했을 때, d(u, v)가 트리의 지름이다.

﻿
import sys
sys.setrecursionlimit(10**6)                                                       # 최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다.

N = int(input())                                                                   # 노드 개수 입력

graph = [[] for _ in range(N+1)]                                                   # 그래프 모델링
for _ in range(N-1):                                                               # 트리의 간선의 개수는 N-1개이므로
    node, child_node, gravity = map(int, sys.stdin.readline().rstrip().split())    # 입력한 노드, 자식노드, 가중치를 그래프에 넣는다.
    graph[node].append((child_node, gravity))                                      
    graph[child_node].append((node, gravity))
    

def dfs(idx, gravity):                                                             # DFS 함수
    for i, j in graph[idx]:                                                        # 현재 위치의 노드 값의 간선을 조회
        if not visited[i]:                                                         # 아직 방문하지 않은 노드는
            visited[i] = True                                                      # 방문처리를 하고
            distance[i] = gravity+j                                                # 거리 리스트에 현재 위치의 노드의 가중치 + 방금 방문처리한 노드의 가중치를 넣는다.
            dfs(i, distance[i])                                                    # 방금 방문처리한 노드로 깊이 탐색 진행 
            

distance = [0] * (N+1)                                                             # 거리를 초기화, 루트 1인 노드의 가중치는 0이므로 겸사 0으로 초기화함
visited = [False] * (N+1)                                                          # 방문여부 초기화
visited[1] = True                                                                  # 루트 1인 노드부터 탐색을 시작할 것이므로 True로 초기화
dfs(1, 0)                                                                          # 루트 1인 노드부터 DFS 탐색 시작
start = distance.index(max(distance))                                              # DFS 탐색이 모두 진행되어 distance에 넣어진 가중치중 제일 큰 노드를 시작 값으로 다시 지정

distance = [0] * (N+1)                                                             # 다시 모든 정점의 거리, 방문여부, 시작 정점으로 지정된 곳만 True로 초기화하고
visited = [False] * (N+1)
visited[start] = True                                                                   
dfs(start, 0)                                                                      # 가중치가 가장 큰 노드부터 다시 DFS 시작
print(max(distance))                                                               # DFS가 종료된 후 가중치가 가장 큰 노드부터 노드들까지의 거리 리스트 중 가장 긴 길이를 출력한다.