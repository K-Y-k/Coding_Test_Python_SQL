# 내가 시도한 방식 - 일부 오답
# 시작하는 정점에서 방문 여부를 모두 초기화 해준후 dfs 탐색을 하였다.

def dfs(idx, count):
    global max_len

    visited[idx] = True

    for v in graph[idx]:
        if not visited[v]:
            dfs(v, count + 1)

    if count > max_len:
        max_len = count


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
max_len = 0

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, 1)

print(max_len)



# 백트래킹을 활용한 dfs
# 각 정점에서 연결된 정점들을 모두 순회하는 모든 경우를 진행해야 하므로
# 다음 정점에서의 순회 때 이동 대상이 되도록 백트래킹으로 현재 위치 방문여부를 다시 취소해준다.

def dfs(idx, count):
    global max_len

    for v in graph[idx]:
        if not visited[v]:
            visited[idx] = True
            dfs(v, count + 1)
            visited[idx] = False

    if count > max_len:
        max_len = count


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
max_len = 0

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    visited[i] = True
    dfs(i, 1)

print(max_len)