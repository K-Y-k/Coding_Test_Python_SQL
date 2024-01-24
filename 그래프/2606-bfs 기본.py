from collections import deque

n = int(input())                                        # 컴퓨터 개수
len_connection = int(input())                           # 연결된 개수 

graph = [[] for _ in range(n+1)]                        # 컴퓨터를 연결한 그래프 초기화
visited = [False] * (n+1)                               # 컴퓨터들의 방문여부 초기화
answer = 0

for _ in range(len_connection):                         # 연결된 개수만큼 입력하여 그래프 모델링
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    global answer

    q = deque()
    q.append(x)                                        # 1번 컴퓨터를 넣는다.
    visited[1] = True                                  # 1번 컴퓨터는 조회했으므로 방분여부 변경

    while q:
        i = q.popleft()
        print('큐 꺼내온 컴퓨터', i)

        for j in graph[i]:
            print('큐 꺼내온 컴퓨터와 연결된 컴퓨터', j)
            if not visited[j]:
                visited[j] = True                     # 현재 컴퓨터는 조회했으므로 방분여부 변경
                answer += 1                           # 현재 컴퓨터 감염됐으므로 카운팅
                q.append(j)                           # 현재 컴퓨터를 큐에 넣기

bfs(1)                                                # 1번 컴퓨터부터 감염시작일 때의 값을 원하므로

print(answer)
