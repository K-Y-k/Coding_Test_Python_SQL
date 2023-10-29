# 행렬 값을 리스트에 넣고
# 각 위치를 차례로 루프를 돌면서 현재 위치의 행, 열을 1~9의 숫자가 중복없이 배치되어 있는지 조사
# 따로 3x3 격자형의 루프를 돌려 조사

T = int(input())

for test_case in range(1, T + 1):
    sudoku_li = []
    answer = 1
    
    for _ in range(9):
    	sudoku_li.append(list(map(int, input().split())))
    
    for i in range(9):
        row_li = []
        col_li = []
        
        # 행 조사
        for j in range(9):
            if sudoku_li[i][j] not in row_li:
                row_li.append(sudoku_li[i][j])
        if len(row_li) < 9:
            answer = 0
        
        # 열 조사
        for j in range(9):
            if sudoku_li[j][i] not in col_li:
                col_li.append(sudoku_li[j][i])
        if len(col_li) < 9:
            answer = 0  
    
    # 3x3 격자 조사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            three_mullti_sudoku = []
            
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if sudoku_li[k][l] not in three_mullti_sudoku:
                        three_mullti_sudoku.append(sudoku_li[k][l])
            if len(three_mullti_sudoku) < 9:
                answer = 0
                    
                
    print('#' + str(test_case), answer)