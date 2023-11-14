# 첫행은 가운데 위치에서부터 시작하므로
# 시작과 끝의 인덱스를 가운데로 지정한 후
# 가운데 행까지는 시작 인덱스는 -1을 하고 끝의 인덱스는 +1을 한 후
# 가운데 행 이후는 시작 인덱스는 +1을 하고 끝의 인덱스는 -1을 한다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    matrix = [list(map(int, input())) for _ in range(N)]
    
    answer = 0
    start = N // 2
    end = N // 2
    
    for i in range(N):
        for j in range(start, end+1):
            answer += matrix[i][j]
            
        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
                
    print('#' + str(test_case), answer)