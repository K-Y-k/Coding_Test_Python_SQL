# DFS 재귀 방식

def solution(n, computers):
    answer = 0
    visited = [False] * n                               # 방문 여부 리스트 선언
    
    def dfs(i):
        visited[i] = True                               # 현재 노드 방문 처리

        for j in range(n):
            if computers[i][j] == 1 and not visited[j]: # 그 다음 노드가 연결되어 있고 방문하지 않았다면
                dfs(j)                                  # 그 다음 노드로 깊이 탐색을 진행한다.
    
    
    for i in range(n):
        if not visited[i]:                              # 방문하지 않았다면
            dfs(i)                                      # 현재 노드로 깊이 탐색을 진행한다.
            answer += 1                                 # 깊이 탐색이 완료되면 네트워크가 모두 형성된 것이므로 카운팅
    
    
    return answer



# BFS 큐 방식

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n                         
    
    def bfs(i):
        q = deque()
        q.append(i)

        while q:                                            # 큐가 빌 때까지 반복
            i = q.popleft()                                 # 현재 노드를 꺼내서
            visited[i] = True                               # 현재 노드 방문처리를 해주고

            for j in range(n):                         
                if computers[i][j] == 1 and not visited[j]: # 그 다음 노드가 연결되어 있고 방문하지 않았다면
                    q.append(j)                             # 그 다음 노드를 큐에 넣어 해당 노드로 너비탐색을 진행한다.
    
    
    for i in range(n):
        if not visited[i]:                   
            bfs(i)                              
            answer += 1                          
    
    
    return answer