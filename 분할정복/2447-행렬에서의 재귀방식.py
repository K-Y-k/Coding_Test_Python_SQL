# 9등분하여 가운데 부분을 제외하고 *을 찍어주면 된다.

N = int(input())                                                      # 행렬 길이 입력
star_list = [[' ' for _ in range(N)] for _ in range(N)]               # 행렬 각 행에 ' '을 행렬 길이 만큼 넣어 모두 공백으로 초기화해놈

def star(x, y, length):                                               # xy좌표와 현재 행렬길이의 매개변수  
    if length == 1:                                                   # 현재 행렬 길이가 1이면 더이상 9등분을 할 수 없으므로 
        star_list[x][y] = '*'                                         # *을 찍어주고
        return                                                        # 반환해 현재 함수를 종료

    for i in range(3):                                                # 길이가 1이 아니면 3*3의 2차원 반복으로 9등분
         for j in range(3):                                           
              if i!=1 or j!=1:                                        # 가운데 부분은 공백으로 비워야하므로 [1][1]로 가운데인 경우만 제외하고
                  star(x+i*(length//3), y+j*(length//3), length//3)   # 재귀 함수를 호출하여 길이가 1이 되어 *을 찍을 때까지 반복할 것이다. 
                    
star(0, 0, N)                                                         # 처음 시작은 0,0,입력길이로 전체의 행렬부터 시작하게 한다.

for i in range(N):                                                    # 2차원 반복으로 행렬 출력
    for j in range(N):
        print(star_list[i][j], end='')                                # 같은 행은 나열해서 출력하고
        
        if j == N-1:                                                  # 같은 행이 끝날 때
            print()                                                   # 행을 띄어준다.

# 위 2차원 반복 출력과 같은 방식
# for i in star_list:
#     print(''.join(i))