# 내가 해본 방식
# BFS 큐 방식을 이용하여
# visited에 이동한 길을 [현재 위치 좌표, 이동된 위치 좌표]와 [이동될 위치 좌표, 현재 위치 좌표]을 넣어두고 
# 현재 좌표가 해당 좌표에 없으면 방문여부를 처리하고 카운팅해준다.

from collections import deque

def solution(dirs):
    answer = 0
    visited = []                         # 방문된 것을 저장하기 위한 리스트 선언
    
    def bfs(x, y, dirs):                 # BFS
        nonlocal answer
        
        q = deque()                      # 큐 선언
        q.append((x,y))                  # 처음 좌표를 넣기
        
        while q:                         # 큐가 빌 때까지 반복
            x, y = q.popleft()           # 제일 앞의 좌표를 가져옴
            
            if dirs[0] == "U":           # 문자에 따라 얼마나 이동됐는지의 좌표 
                temp_x = -1
                temp_y = 0
            elif dirs[0] == "D":
                temp_x = 1
                temp_y = 0
            elif dirs[0] == "L":
                temp_x = 0
                temp_y = -1
            elif dirs[0] == "R":
                temp_x = 0
                temp_y = 1
                
            nx = x + temp_x              # 현재 좌표에서 이동하는 만큼 적용
            ny = y + temp_y
            
            if 0<=nx<=10 and 0<=ny<=10:  # 문제에서 주어진 범위에 벗어나지 않았을 경우
                q.append((nx, ny))       # 이동된 좌표로 큐에 넣어두고
                
                if [(x,y), (nx,ny)] not in visited and [(nx,ny), (x,y)] not in visited: # 방문 리스트에 해당 좌표 이동이 없었다면
                    visited.append([(x,y), (nx,ny)])                                    # 방문 리스트에 저장하고
                    visited.append([(nx,ny), (x,y)])
                    answer += 1                                                         # 새로운 길이므로 정답에 카운팅
            else:
                q.append((x, y))
                    
                    
            if len(dirs) > 1:                                                          # 위에서 현재 명령을 다 처리했으므로 다음 문자로 적용
                dirs = dirs[1:]
            else:
                break
    
    bfs(5, 5, dirs)                                                                    # 한 가운데에서 시작하므로 5,5로 넣어 BFS 시작
    
    
    return answer



# set을 이용한 방식

def solution(dirs):
    answer = 0
    visited = set()
    
    def bfs(x, y, dirs):
        nonlocal answer
        
        q = deque()
        q.append((x,y))
        
        while q:
            x, y = q.popleft()
            
            if dirs[0] == "U":
                temp_x = -1
                temp_y = 0
            elif dirs[0] == "D":
                temp_x = 1
                temp_y = 0
            elif dirs[0] == "L":
                temp_x = 0
                temp_y = -1
            elif dirs[0] == "R":
                temp_x = 0
                temp_y = 1
                
            nx = x + temp_x
            ny = y + temp_y
            
            if 0<=nx<=10 and 0<=ny<=10:
                q.append((nx, ny))
                move1 = (x, y, nx, ny)
                move2 = (nx, ny, x, y)
                
                if move1 not in visited and move2 not in visited:
                    visited.add(move1)
                    visited.add(move2)
                    answer += 1
            else:
                q.append((x, y))
                    
                    
            
            if len(dirs) > 1:
                dirs = dirs[1:]
            else:
                break
    
    bfs(5, 5, dirs)
    
    
    return answer