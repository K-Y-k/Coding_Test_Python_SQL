# DFS 재귀 방식
# 처음에 출발하는 항공, 거쳐가는 경로를 dfs에 넣어
# 출발하는 항공이 같고 아직 방문하지 않은 항공권이면
# 해당 항공권의 도착지, 거쳐가는 경로를 넣어 깊이 탐색을 진행한다.
# 거쳐가는 경로의 길이가 티켓 길이 + 1이면 모든 티켓을 사용하게 된 것이므로 정답 리스트에 해당 경로를 넣어준다.
# 이렇게 모든 경로들이 저장된 정답 리스트에서 알파벳이 작은 기준으로 정렬하게하여 
# 제일 첫 원소의 경로가 알파벳이 작은 순서의 경로이다. 

def solution(tickets):
    answer = []
    
    m = len(tickets)
    visited = [False] * m
    
    def dfs(start, path):
        if len(path) == m+1:                      # 거쳐가는 경로의 길이가 티켓 길이 + 1이면
            answer.append(path)                   # 모든 티켓을 사용하게 된 것이므로 정답 리스트에 해당 경로를 넣어준다.
            return
        
        
        for idx, ticket in enumerate(tickets):
            if start == ticket[0] and visited[idx] == False:    # 출발하는 항공이 같고 아직 방문하지 않은 항공권이면
                visited[idx] = True                             # 방문 처리를 해주고
                dfs(ticket[1], path + [ticket[1]])              # 해당 항공권의 도착지, 거쳐가는 경로를 넣어 깊이 탐색을 진행한다.
                visited[idx] = False                            # 끝까지 깊이 탐색이 완료되었으면 방문 처리 했던 것을 백트랙킹 해준다.
        
        
    dfs("ICN", ["ICN"])                           # 처음에 출발하는 항공, 거쳐가는 경로를 dfs에 넣고 진행
    
    
    answer.sort()                                 # 이렇게 모든 경로들이 저장된 정답 리스트에서 알파벳이 작은 기준으로 정렬하게하여 
   
    return answer[0]                              # 제일 첫 원소의 경로가 알파벳이 작은 순서의 경로이다. 