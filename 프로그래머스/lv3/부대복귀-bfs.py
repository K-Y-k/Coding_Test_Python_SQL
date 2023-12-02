# 기준을 강철부대인 목적지에서 부터 탐색해 나가며 거리를 갱신해야한다!
# 내가 부족했던 점은 주어진 부대원의 위치에서부터 목적지까지 탐색하려고 시도했기 때문에 잘 안된 것

from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n+1)]              # 서로 지역 연결된 위치 그래프
    visited = [False] * (n+1)                     # 방문여부
    distance = [-1] * (n+1)                       # 거리    : -1인 이유는 목적지로 복귀 못하는 부대원은 -1로 출력하라고 했기 때문
    
    visited[destination] = True                   # bfs를 목적지에서부터 진행할 것이기에 목적지에서의 방문여부 갱신
    distance[destination] = 0                     #                                    목적지에서의 거리 갱신
    
    
    for a, b in roads:                            # 그래프 형성
        graph[a].append(b)
        graph[b].append(a)
    
    
    def bfs(x):                                   # 큐 생성
        q = deque()                               # 큐 생성
        q.append(x)                               # 처음 시작하는 목적지 값 넣기
        
        
        while q: 
            a = q.popleft()                       # 큐에서 지역노드 값을 꺼내고
            
            for i in graph[a]:                    # 해당 지역에 연결된 지역 노드들을 조회해가며
                if not visited[i]:                # 방문하지 않았다면
                    distance[i] = distance[a] + 1 # 현재 순회한 위치의 거리를 해당 지역의 위치의 값에서 +1을 갱신해준다.
                    visited[i] = True             # 방문처리
                    q.append(i)                   # 현재 순회한 위치 큐에 넣기
    
    bfs(destination)                              # 목적지 값을 넣고 bfs 진행
    
    
    for i in sources:                             # 부대원이 위치한 지역을 조회하여
        answer.append(distance[i])                # bfs에서 갱신한 지역에서 목적지까지의 거리를 정답에 넣기
        
    
    return answer