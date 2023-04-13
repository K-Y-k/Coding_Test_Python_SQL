import sys

N = int(input())                                                                      # 행렬의 길이 입력

paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]         # 행렬의 길이만큼 반복해서 각 행에 삽입

result_minusOne = 0                                                                   # 결과 변수들 초기화
result_zero = 0
result_one = 0

def divideConquer(x, y, length):                                                      # 재귀 방식의 분할정복 함수(행 위치, 열 위치, 행 길이)
    global result_minusOne, result_zero, result_one                                   # global로 전역변수들 가져옴
    
    number = paper_list[x][y]                                                         # 현재 위치 즉 제일 앞의 값을 기준 숫자로 설정
    for i in range(x, x+length):                                                      # 현재위치x,y+행렬길이로 반복을 돌려 탐색
        for j in range(y, y+length):                                                    
            if paper_list[i][j] != number:                                            # 탐색한 위치의 숫자가 기준 숫자와 다르면
                for k in range(3):                                                    # 9등분으로 나누기 위해 3x3의 2차원 루프로
                    for l in range(3):
                        divideConquer(x+k*(length//3), y+l*(length//3), length//3)    # 재귀함수 호출
                return                                                                # 모든 반복이 끝나고 모두 호출되면 반환
            
    if number == -1:                                                                  # 위 탐색에서 기준 숫자와 모두 동일했을 경우 기준 숫자의 숫자 결과에 카운팅 
        result_minusOne += 1
    elif number == 0:
        result_zero += 1
    elif number == 1:
        result_one += 1
        
divideConquer(0, 0, N)                                                                # 첫 위치 x:0, y:0, 처음 입력했던 행렬의 길이부터 재귀함수 시작하여
print(result_minusOne)                                                                # 모두 마친 결과 값들 출력
print(result_zero)
print(result_one)