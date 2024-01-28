# 벽을 3곳을 설치한 후 바이러스를 퍼트리고 감염되지 않은 개수의 최대 값을 구하려면
# 벽을 3곳을 설치하고 bfs로 바이러스를 퍼트린 후 다시 벽 3곳을 원상태로 복구해야하므로 백트래킹이 필요하다.

from collections import deque
import copy

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
count_li = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def makeWall(count):
    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1                  # 벽을 설치하고
                makeWall(count + 1)              # 벽이 3곳 설치한 후 bfs가 진행되도록 재귀호출하고
                graph[i][j] = 0                  # 현재 벽 3곳을 설치한 경우가 끝났으므로 다시 벽을 제거한다.


def bfs():
    q = deque()
    tmp_graph = copy.deepcopy(graph)             # 복사 방식1
    # tmp_graph = [row[:] for row in graph]      # 복사 방식2

    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    q.append((nx, ny))

    count = 0
    for i in range(N):
        count += tmp_graph[i].count(0)

    count_li.append(count)


makeWall(0)

print(max(count_li))