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