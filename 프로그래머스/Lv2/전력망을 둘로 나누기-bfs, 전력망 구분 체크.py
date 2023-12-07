# 전력망을 나눴는지에 대한 구분할 리스트가 필요하다.
# 기존 그래프를 형성한 후 
# 와이어를 조회하면서의 연결된 두 노드의 전력망을 끊은 후에 bfs로 탐색하여 두 노드에서의 연결된 개수를 카운팅한 후
# 다시 

from collections import deque 

def solution(n, wires):
    answer = n
    
    check_link = [[True]*(n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    
    for i, j in wires:
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
                if not visited[i] and check_link[x][i]:
                    visited[i] = True
                    count += 1
                    q.append(i)
    
        return count
    
    
    for a, b in wires:
        visited = [False] * (n+1)
        check_link[a][b] = False
        count1 = bfs(a)
        count2 = bfs(b)
        check_link[a][b] = True
        
        answer = min(answer, abs(count1 - count2))
        
        
    return answer