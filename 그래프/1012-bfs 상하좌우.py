# 문제의 의도는 배추가 심어진곳 기준으로 상하좌우에 배추가 있는 곳까지 하나의 지렁이가 역할을 맡으므로
# 방문하지 않았고 배추인 곳이면 그 배추위치부터 인접한 배추까지 방문한 후 지렁이를 심어야하는 곳이므로 카운트하면 된다.

from collections import deque

def bfs(i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <=nx<N and 0<=ny<M:
                if not visited[nx][ny] and graph[x][y] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    require_count = 0

    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:            # 방문하지 않았고 배추인 곳이면
                bfs(i, j)                                         # 그 배추위치부터 인접한 배추까지 방문한 후
                require_count += 1                                # 지렁이를 심어야하는 곳이므로 카운트하면 된다.

    print(require_count)