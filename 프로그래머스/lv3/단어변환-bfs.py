# 너비 우선 탐색으로 글자가 하나만 다른 경우 
# 방문 처리 후 현재 단어와 거친 단계수를 넣으면서 진행했다.

# 유의점: 카운팅을 큐에 넣지 않고 따로 변수를 두어 카운팅 처리하지말자 (맞지 않은 단어까지 카운팅될 수 있어 큐에 카운트 값도 같이 넣어주자)
              

from collections import deque

def solution(begin, target, words):
    n = len(words)
    visited = [False] * n
    
    
    def bfs(begin):
        q = deque()
        q.append((begin, 0))
        
        while q:
            word, count = q.popleft()                         # 현재 단어와 거친 단계수를 꺼내오고
            
            if word == target:                                # 현재 단어가 만약 목표 단어이면
                return count                                  # 총 거친 단계 수를 반환
            
            
            for i in range(n):                                # 현재 단어
                if not visited[i]:                            # 아직 방문하지 않았고
                    diff_count = 0

                    for j in range(len(words[i])):
                        if words[i][j] != word[j]:            # 같은 자리의 위치 단어가 다를 경우
                            diff_count += 1                   # 카운팅
                            
                    if diff_count == 1:                       # 카운팅한 개수가 하나만 다른 경우
                        visited[i] = True                     # 방문 처리 후
                        q.append((words[i], count+1))         # 현재 단어와 거친 단계수 최신화해서 큐에 넣어준다.
                                                              # 유의점: 카운팅을 큐에 넣지 않고 여기서 따로 변수를 두어 +1 처리하지말자 (맞지 않은 단어까지 카운팅될 수 있어 큐에 카운트 값도 같이 넣어주자)
            
            
    if target not in words:                                   # 목표 단어가 리스트에 없을 경우 
        return 0                                              # 0 반환
    else:                                                     # 있을 경우
        return bfs(begin)                                     # bfs 문제에서 시작되는 단어를 넣고 시작