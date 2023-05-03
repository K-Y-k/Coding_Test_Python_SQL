# 방문여부 visited를 여기서는 알파벳을 기준으로 설정했다.
# 기존에 풀었던 deque를 활용한 BFS로는 시간초과가 발생한다.
# 알파벳의 중복을 방지하려면 set()을 활용해야한다.
# set은 추가할 때 append가 아닌 add로 해야하고 popleft()가 아닌 pop()으로 꺼내야한다.


# BFS 방식
import sys

R, C = map(int, input().split())                                  # 행, 열 입력
graph = [list(sys.stdin.readline().strip()) for _ in range(R)]    # 그래프 모델링
alphabet = set()                                                  # 방문여부를 알파벳 기준으로 설정
count = 1                                                         # 무조건 1칸은 이동가능하므로 1로 초기화

dx = [-1, 1, 0, 0]                                                # 상하좌우 이동 지정
dy = [0, 0, -1, 1]


def bfs(x, y, alpha):
    global count
    q = set()                                     # 시간 초과를 줄이기 위해 중복되는 곳은 제거되는 set()활용
    q.add((x, y, alpha))                          # 초기 값을 넣음
    
    while q:                                      # 큐가 빌 때까지
        x, y, alphabet = q.pop()                  # pop()으로 x, y, 현재까지의 알파벳을 꺼낸다.
        count = max(count, len(alphabet))         # 지금까지 갱신된 총 이동횟수와 현재까지 이동한 횟수중 제일 큰 값으로 갱신 (alphabet은 중복되지 않게 설정하여 결국 alphabet의 길이가 지금까지 이동한 칸의 횟수랑 동일하다)

        for i in range(4):                        # 상/하/좌/우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<R and 0<=ny<C:               # 범위 내에 있고 알파벳이 중복이 안된다면 탐색
                if graph[nx][ny] not in alphabet:
                    q.add((nx, ny, alphabet + graph[nx][ny]))
                

bfs(0, 0, graph[0][0])                            # 첫 초깃값으로 BFS 시작
print(count)



# DFS 방식 = 시간 초과
# BFS에서는 중복 경로를 제거해줬지만
# DFS에서는 중복 경로를 제거하지 못하고 완전 탐색을 하느라 시간 초과가 나온 것 같다.
import sys

R, C = map(int, input().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(R)]
alphabet = set()
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, count):
    global result
    result = max(result, count)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<R and 0<=ny<C:
            if graph[nx][ny] not in alphabet:
                alphabet.add(graph[nx][ny])
                dfs(nx, ny, count+1)
                alphabet.remove(graph[nx][ny])

alphabet.add(graph[0][0])
dfs(0, 0, 1)
print(result)
