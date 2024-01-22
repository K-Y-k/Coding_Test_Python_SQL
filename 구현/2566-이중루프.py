# 입력을 받고
# 모두 조회하며 최대값일 때 새로 값,행,열을 새로 갱신해간다.


# matrix = [[0]*9 for _ in range(9)]
# for i in range(9):
#     a_li = list(map(int, input().split()))
    
#     for j in range(9):
#         matrix[i][j] = a_li[j]
matrix = [list(map(int, input().split())) for _ in range(9)] # 위 코드를 한 줄로 표현

max_num = 0;
row = 0;
col = 0;

for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max_num:              # 최대값이 같을 수 있으므로 크거나 같아야 한다.
            max_num = matrix[i][j]
            row = i+1
            col = j+1
            
print(max_num)
print(row, col)