# 그래프를 형성한 후
# 방문여부와 거리를 노드 개수만큼 초기화한 후
# 노드 1부터 거리가 제일 먼 노드들을 탐색해야하므로
# bfs로 노드 1부터 큐에 넣고 노드1에 엮인 노드부터 조회해가며 현재 노드의 거리를 갱신해간다.
# 갱신한 노드 위치의 거리들을 조회하면서 최대 값보다 크면 제일 먼 거리이므로 정답에 카운팅

from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)              # 방문여부와
    distance = [-1] * (n+1)                # 거리를 노드 개수만큼 초기화한 후
    
    
    for i, j in edge:                      # 그래프를 형성한 후
        if j not in graph[i]:
            graph[i].append(j)
            
        if i not in graph[j]:
            graph[j].append(i)
    
    
    def bfs(x):
        q = deque()
        q.append(x)                                  # 첫 노드를 넣고
        
        while q:                                     
            x = q.popleft()
            
            for i in graph[x]:
                if not visited[i]:                   # 방문하지 않았으면
                    visited[i] = True                # 방문여부 갱신
                    distance[i] = distance[x] + 1    # 현재 노드의 거리 갱신
                    q.append(i)                      # 현재 노드 큐에 넣기
    

    visited[1] = True                                # 노드 1부터 거리가 제일 먼 노드들을 탐색해야하므로 노드 1일 때의 방문여부와
    distance[1] = 0                                  # 거리를 초기화
    
    bfs(1)                                           # 노드 1일 때의 bfs 진행
    
    for i in distance:                               # 갱신한 노드 위치의 거리들을 조회하면서
        if i == max(distance):                       # 최대 값보다 크면 제일 먼 거리이므로
            answer += 1                              # 정답에 카운팅
    
    
    return answer