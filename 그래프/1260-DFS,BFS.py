from collections import deque                        # BFS에서 큐처럼 활용하기 위해 deque 라이브러리 선언
import sys

N, M, start = map(int, input().split())

relation = [[] for _ in range(N+1)]                  # 인접리스트 방식의 간선 리스트 선언
visited = [False] * (N+1)                            #  방문 여부 리스트 선언

for _ in range(M):                                   #  입력된 관계를 간선 리스트에 채움
    a, b = map(int, sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)
    
for i in range(1, N+1):                              # 연결요소들을 모두 오름차순으로 정렬
    relation[i].sort()
    

def dfs(idx):                                        # 재귀호출을 활용한 DFS 함수
    global visited                                   # 전역변수를 사용하기 위해 global로 가져옴
    visited[idx] = True
    print(idx, end=' ')
    
    for i in relation[idx]:                          # 방문을 하지 않은 노드는 재귀호출 방식으로 깊이 탐색 진행
        if not visited[i]:
            dfs(i)

def bfs(idx):                                        # 큐를 활용한 BFS 함수
    q = deque()                                      # 큐 생성
    q.append(idx)                                    # 큐의 시작하는 정점의 값을 넣는다.
    visited[idx] = True
  
    while q:                                         #  큐가 비어있을 때까지 반복
        x = q.popleft()                              # 큐의 앞쪽의 정점 값을 꺼내고
        print(x, end=' ')
        
        for i in relation[x]:                        # 꺼낸 정점에 연결된 노드 중  
            if not visited[i]:                       # 방문을 하지 않은 노드
                visited[i] = True                    # 방문처리 후
                q.append(i)                          # 큐의 뒤쪽에 넣는다.

dfs(start)
print()

visited = [False] * (N+1)                            # DFS로 이미 방문이 진행되었으므로 BFS로 새로 시작하기위해 초기화
bfs(start)