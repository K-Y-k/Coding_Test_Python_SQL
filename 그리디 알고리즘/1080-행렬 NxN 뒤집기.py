# 3x3으로 뒤집어서 같아지기까지 뒤집은 최소 횟수를 구하는 것이므로 입력한 행렬이 3x3보다 작으면 -1이다.
# for문을 3x3으로 뒤집어야하므로 현재위치의 x~x+3과 현재위치의 y~ y+3의 범위로 뒤집는다.
# 3x3보다 크면 3x3씩 검사하므로 검사할 때 x와 y의 끝인 위치는 N-2, M-2까지이다. 
# 그래야  위 처럼 3x3을 검사할 때 인덱스가 벗어나지 않는다.


N, M = map(int, input().split())                                  # 행, 열 입력

A_procession = [list(map(int, list(input()))) for _ in range(N)]  # A행렬 선언 및 입력
B_procession = [list(map(int, list(input()))) for _ in range(N)]  # B행렬 선언 및 입력

def reverse(x, y):                                                # A행렬을 뒤집는 함수 선언
    for i in range(x, x+3):                                       # 3x3을 뒤집으므로 각 현재 위치x,y에서 +3까지
        for j in range(y, y+3):
            if A_procession[i][j] == 0:                           # 0은 1로 뒤집고
                A_procession[i][j] = 1
            else:                                                 # 1은 0으로 뒤집는다.
                 A_procession[i][j] = 0
                    
count = 0

if (N < 3 or M < 3) and A_procession != B_procession:             # 주어진 A,B행렬이 같지 않는데도 3x3으로 뒤집을 수 없을 정도로 작은 행렬인 경우
    print(-1)                                                     # -1 출력
else:                                                             # 뒤집을 수 있는 행렬 크기이면
    for x in range(N-2):
        for y in range(M-2):
            if A_procession[x][y] != B_procession[x][y]:          # 현재 x,y위치에서 다르면
                count += 1                                        # 뒤집는 count를 증가시키고
                reverse(x, y)                                     # A행렬을 뒤집는 함수 호출.
                
if A_procession != B_procession:                                  # 모두 돌려도 같지 않으면 -1 출력
    print(-1)
else:                                                             # 같아진 상황이면
    print(count)                                                  # 위에서 연산적용된 count 출력