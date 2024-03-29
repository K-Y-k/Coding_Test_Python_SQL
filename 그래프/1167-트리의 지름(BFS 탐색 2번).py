from collections import deque
import sys

V = int(input())

graph = [[] for _ in range(V+1)]                                               # 그래프 모델링            
for _ in range(V):                                                             # 트리의 간선의 개수는 V-1개이지만 여기서는 정점의 번호를 기준으로 삽입하므로 노드 개수에 맞춰야한다.
    node_list = list(map(int, sys.stdin.readline().rstrip().split())) 
    
    for i in range(1, len(node_list)-1, 2):                                    # 문제에서 해당 노드에 연결된 노드 번호와 가중치 2개가 1쌍으로 입력되므로 2칸씩의 간격을 넘으며 루프를 돌려야한다. 
        if node_list[i] == -1:                                                 # -1이면 입력된 내용이 끝났으므로 종료
            break
        else:                                                                  # -1이 아니면 1쌍의 내용(연결된 노드, 가중치)을 삽입
            graph[node_list[0]].append((node_list[i], node_list[i+1]))  
    

def bfs(start):                                                                # BFS 함수
    q = deque()                                                                # 큐 선언 및 시작 값 삽입 
    q. append(start)
    
    while q:                                                                   # 큐가 빌 때까지
        idx = q.popleft()                                                      # 제일 앞의 원소를 꺼내와서 
        
        for i, j in graph[idx]:                                                # 꺼낸 원소와 연결된 원소들을 조회하고
            if not visited[i]:                                                 # 아직 방문한적이 없는 원소이면
                visited[i] = True                                              # 방문처리를 하고
                distance[i] = distance[idx] + j                                # 거리 리스트에 꺼낸원소의 가중치 + 방문처리한 노드의 가중치를 넣는다.
                q.append(i)                                                    # 방문처리한 노드를 큐에 넣는다.
                
distance = [0] * (V+1)                                                         # 거리를 초기화, 루트 1인 노드의 가중치는 0이므로 겸사 0으로 초기화함
visited = [False] * (V+1)                                                      # 방문여부 초기화
visited[1] = True                                                              # 루트 1인 노드부터 탐색을 시작할 것이므로 True로 초기화
bfs(1)                                                                         # 루트 1인 노드부터 BFS 탐색 시작
start = distance.index(max(distance))                                          # BFS 탐색이 모두 진행되어 distance에 넣어진 가중치중 제일 큰 노드를 시작 값으로 다시 지정

distance = [0] * (V+1)                                                         # 다시 모든 정점의 거리, 방문여부, 시작 정점으로 지정된 곳만 True로 초기화하고
visited = [False] * (V+1)
visited[start] = True
bfs(start)                                                                     # 가중치가 가장 큰 노드부터 다시 BFS 시작
print(max(distance))                                                           # BFS로 각 거리가 지정된 거리 리스트에서 가중치가 가장 큰 노드부터 노드들까지의 거리 리스트 중 가장 긴 길이를 출력한다.