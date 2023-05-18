# 문제에서 도화지 100 x 100으로 주어진 이유를 생각해야한다.

# 100 x 100 도화지 안에서 10 x 10의 도형이 붙여지는 것이므로 
# 주어진 x좌표~주어진 x좌표+10까지, 주어진 y좌표~주어진 y좌표+10) 범위까지 해당 위치 값 1로 만들고
# 100 x 100 전체를 조회하여 1인 것만 카운팅하면 결국 총 넓이가 된다. 

# 넓이를 이런 방식으로 생각하는 것이 어려웠다.



import sys

N = int(input())

paper_position = [[0]*100 for _ in range(100)]                # 100x100의 도화지의 각 모든 값을 0으로 초기화

for _ in range(N):
    y, x = map(int, sys.stdin.readline().rstrip().split())    # 가로, 세로순으로 주어지므로 x를 세로 기준으로 생각하려면 y,x로 선언  
    
    for i in range(x, x+10):                                  # 위 주어진 좌표에 +10까지의 범위가 도형이므로 2중 루프를 돌려
        for j in range(y, y+10):
            paper_position[i][j] = 1                          # 해당 위치의 값은 1로 표기하여 넓이로 취급하기
            
count = 0                                                     # 총 넓이를 셀 변수 선언

for i in range(100):                                          # 100x100 도화지 전체를 조회하여
    for j in range(100):
        if paper_position[i][j] == 1:                         # 1로 표시된 것은 넓이라고 했으므로
            count += 1                                        # 총 넓이에 카운팅

print(count)                                                  # 총 넓이 출력