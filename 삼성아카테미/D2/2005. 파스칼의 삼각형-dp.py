# dp처럼 각 위치에 미리 0으로 초기화 시켜놓고
# 초깃값을 넣은 후에 for문으로 문제에서 주어진 원칙의 점화식을 적용시켜간다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    pascal = [[0] * N for _ in range(N)]
    
    pascal[0][0] = 1
    
    for i in range(1, N):
        for j in range(N):
            if j == 0:
                pascal[i][j] = 1
            else:
            	pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#' + str(test_case))
    for i in range(N):
        for j in range(N):
            if pascal[i][j] != 0:
                print(pascal[i][j], end=' ')
        
        print()