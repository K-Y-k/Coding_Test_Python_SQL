import sys
sys.setrecursionlimit(10**6)

def dfs(idx):                                                                 # 사이클을 찾기 위한 깊이 탐색 DFS 함수 선언
    global result                                                             # 결과 변수 전역 값 그대로 가져옴
    visited[idx] = True                                                       # 방문여부 표시
    cycle.append(idx)                                                         # 사이클 리스트에 현재 값 넣기
    
    next_idx = stu_no[idx]                                                    # 현재 위치의 정점이 가리키는 다른 정점인 다음 노드 가져오기

    if visited[next_idx]:                                                     # 다음 노드가 이미 방문처리가 되었으면 깊이탐색을 모두 한 상황으로
        if next_idx in cycle:                                                 # 다음 노드가 사이클 리스트에 이미 넣어져있어야 사이클이 형성된 상태인 것이므로
            result += cycle[cycle.index(next_idx):]                           # 결과 변수에 사이클이 형성된 노드들만 넣기

        return                                                                # 사이클 리스트에 없으면 사이클이 형성된 것이 아니므로 그냥 아무 값 없이 반환
   
    else:                                                                     # 다음 노드가 방문처리가 되어있지 않으면 계속 깊이 탐색해야하는 노드이므로
        dfs(next_idx)                                                         # 깊이 탐색 재귀호출
    
    
T = int(input())                                                              # 테스트 케이스 입력
for _ in range(T):                                                            # 입력한 값 만큼 테스트 반복
    n = int(sys.stdin.readline().rstrip())                                    # 학생 수 입력
    
    visited = [False] * (n+1)                                                 # 방문처리여부와 각 학생이 연결된 그래프 입력과 결과 변수 초기화
    stu_no = [0] + list(map(int, sys.stdin.readline().rstrip().split()))      # 인덱스를 맞추기 위해 [0] + 한 것
    result = []
    
    for i in range(1, n+1):                                                   # 학생수인 1부터 n까지 반복
        if not visited[i]:                                                    # 처음 방문하는 것이면
            cycle = []                                                        # 사이클 리스트를 초기화하고
            dfs(i)                                                            # DFS 진행
    
    print(n-len(result))                                                      # DFS가 모두 마친 상황으로 result에는 사이클이 형성된 학생들만 들어가 있으므로 전체 - 팀프로젝트를 꾸린 학생수로 결과 출력