# N x N의 행렬 값을 넣고
# N x N의 행렬의 각 위치에서의 M x M크기의 행렬의 값들을 합산한 값을 리스트에 넣고
# 합산한 값들의 리스트에서의 최대 값을 출력하면 된다.

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    
    # N x N의 행렬 값을 넣고
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
        

    total_li = []     
   
    for i in range(N-M+1):                      # N x N의 행렬의 각 위치에서의
        for j in range(N-M+1):
            total = 0

            for k in range(M):                  # M x M크기의 행렬의 값들을
                for l in range(M):
                    total += matrix[i+k][j+l]   # 합산한 값을
                
            total_li.append(total)              # 리스트에 넣고
    
    print('#' + str(test_case), max(total_li))  # 합산한 값들의 리스트에서의 최대 값을 출력하면 된다.