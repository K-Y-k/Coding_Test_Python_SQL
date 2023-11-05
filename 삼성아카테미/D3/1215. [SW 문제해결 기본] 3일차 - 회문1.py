# 내가 시도한 방식 
# 각 위치에서부터 각 가로, 세로 + 주어진 길이 만큼의 문자를 거꾸로 만든 문자와 비교하여 같으면 카운팅 

for test_case in range(1, 11):
    N = int(input())
    matrix = []
    answer = 0
    
    for _ in range(8):
        matrix.append(list(input()))
    
    for i in range(8):
        for j in range(8-N):
            # 가로 비교
            col_ = ''
            
            for k in range(N):
                col_ += matrix[i][j+k]
            
            if col_ == col_[::-1]:
                answer += 1
            
            
            # 세로 비교
            if i < 8-N:
                row_ = ''

                for k in range(N):
                    row_ += matrix[i+k][j]

                if row_ == row_[::-1]:
                    answer += 1
            
            
    print('#' + str(test_case), answer)



# 정답

for test_case in range(1, 11):
    N = int(input())
    matrix = []
    answer = 0
    
    for _ in range(8):
        matrix.append(list(input()))
    
    for i in range(8):
        for j in range(8-N+1):
            # 가로 비교
            col_ = ''
            for k in range(N):
                col_ += matrix[i][j+k]
                
            if col_ == col_[::-1]:
                answer += 1
            

            # 세로 비교
            row_ = ''
            for k in range(N):
                row_ += matrix[j+k][i]  # 세로의 경우 row 인덱스와 col 인덱스 주의

            if row_ == row_[::-1]:
                answer += 1
            
            
    print('#' + str(test_case), answer)