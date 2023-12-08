# 전력망을 끊었는지에 대한 구분할 리스트가 필요하다.
# 와이어를 통해 기존 그래프를 형성한 후
# 와이어를 조회하면서 연결된 두 노드의 전력망을 끊은 후에 두 노드 기준으로 bfs로 탐색하여 두 노드에서의 연결된 개수를 카운팅한 후
# 다시 끊은 것을 이어붙힌 후 최솟값인지 확인한다.

from collections import deque 

def solution(n, wires):
    answer = n
    
    check_link = [[True]*(n+1) for _ in range(n+1)]             # 전력망을 끊었는지에 대한 구분할 리스트가 필요하다.
    graph = [[] for _ in range(n+1)]
    
    for i, j in wires:                                          # 와이어를 통해 기존 그래프를 형성한 후
        graph[i].append(j)
        graph[j].append(i)
    
    
    def bfs(x):                                                 
        q = deque()
        q.append(x)
        
        visited[x] = True
        count = 1
        
        while q:
            a = q.popleft()                                    
            
            for i in graph[a]:
                if not visited[i] and check_link[x][i]:        # 연결된 개수를 카운팅
                    visited[i] = True
                    count += 1
                    q.append(i)
    
        return count
    
    
    for a, b in wires:                                         # 와이어를 조회하면서 노드에서의 연결된 개수를 카운팅한 후
        visited = [False] * (n+1)
        check_link[a][b] = False                               # 연결된 두 노드의 전력망을 끊은 후
        count1 = bfs(a)                                        # 두 노드 기준으로 bfs로 탐색하여
        count2 = bfs(b)
        check_link[a][b] = True                                # 다시 끊은 것을 이어붙힌 후
        
        answer = min(answer, abs(count1 - count2))             # 최솟값인지 확인한다.
        
        
    return answer