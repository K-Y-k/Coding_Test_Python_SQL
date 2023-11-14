# 열라인, 행라인, 대각선1라인, 대각선2라인 각 케이스에 맞체 적용해주기

T = 10

for test_case in range(1, T + 1):
    a = int(input())
    matrix = []
    
    for _ in range(100):
        matrix.append(list(map(int, input().split())))
    
    max_count = 0                      # 최대 값
    cross_a = 0                        # 대각선1의 합을 위한 초기화
    cross_b = 0                        # 대각선2의 합을 위한 초기화
    
    for i in range(100):
        col = sum(matrix[i])           # 열라인의 합 적용
        row = 0                        # 행라인의 합을 위한 초기화

        cross_a += matrix[i][i]        # 대각선1의 합 적용 
        cross_b += matrix[99-i][i]     # 대각선2의 합 적용
        
        for j in range(100):
            row += matrix[j][i]        # 행라인의 합 적용
    
        if i == 99:                                                # 마지막 행일 경우
            max_count = max(col, row, max_count, cross_a, cross_b) # 대각선까지 모두 합해진 값까지 같이 비교
        else:                                                      # 그 외의 행은
            max_count = max(col, row, max_count)                   # 열, 행의 합 중 최대 값
            
        
    print('#' + str(test_case), max_count)
    