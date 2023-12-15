# 내가 푼 방식 : 일부 테케 실패
# 거리를 적용하면서 K보다 작으면 배달이 가능한 노드이므로 노드를 정답에 넣게하여 
# 총 길이를 정답으로 나오게 했으나 일부 문제 발생

from collections import deque

def solution(N, road, K):
    answer = [1]
    
    graph = [[] for _ in range(N+1)]
    
    for i, j, c in road:
        graph[i].append((j, c))
        graph[j].append((i, c))
    
    
    def bfs(x, c1):
        q = deque()
        q.append((x, c1))
        
        if c1 <= K and x not in answer:
            answer.append(x)
        
        while q:
            x, cost = q.popleft()
            
            for i, c2 in graph[x]:
                if cost + c2 <= K:
                    q.append((i, cost + c2))
                    
                    if i not in answer:
                        answer.append(i)
                    

    for i, c in graph[1]:
        bfs(i, c)
    
    
    return len(answer)



# 최소 거리로 갱신하기 위해 거리 리스트를 따로 활용하고
# 방문하지 않은 경우(=거리가 0)이거나 거리 리스트의 최근 갱신된 현재 노드의 거리 값보다 작으면
# 노드와 거리를 갱신한 값을 큐에 넣고 거리 리스트의 현재 노드 인덱스에서의 거리를 최신화한다.

from collections import deque

def solution(N, road, K):
    
    graph = [[] for _ in range(N+1)]
    
    for i, j, c in road:
        graph[i].append((j, c))
        graph[j].append((i, c))

    distance = [0 for _ in range(N+1)]
    
    
    def bfs(x):
        q = deque()
        q.append((x, 0))
        distance[1] = 1

        while q:
            x, cost = q.popleft()

            for i, c in graph[x]:
                if distance[i] == 0 or cost + c < distance[i]:
                    q.append((i, cost + c))
                    distance[i] = cost + c
                
    bfs(1)
    
    answer = 0
    
    for i in distance:
        if i != 0 and i <= K:
            answer += 1
    
    
    return answer