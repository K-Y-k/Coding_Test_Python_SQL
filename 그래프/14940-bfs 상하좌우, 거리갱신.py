# 목적지에서부터 상하좌우 bfs를 시작하여 거리를 갱신해나간다.
# 주의점은 0으로 둘러쌓인 1인 곳은 도착할 수 없는 거리라서 -1로 표기하도록 처리해야한다! 


from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
distance = [[0] * M for _ in range(N)]


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
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))


for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            bfs(i, j)
            break

# 주의점은 0으로 둘러쌓인 1인 곳은 도착할 수 없는 거리라서 -1로 표기하도록 처리해야한다! 
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            distance[i][j] = -1

for i in range(N):
    print(' '.join(map(str, distance[i])))
