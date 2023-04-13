import sys
N = int(input())                                                                 # 행렬의 길이 입력

quad_tree = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]    # 행렬 길이 만큼 각 행의 내용 입력

def divideConquer(x, y, length):                                                 # 행x, 열 y, 행렬의 길이 length
    number = quad_tree[x][y]                                                     # 첫번째 값을 기준 숫자로 지정 
    
    for i in range(x, x+length):                                                 # 현재위치x,y+행렬길이로 반복을 돌려 탐색
        for j in range(y, y+length):
            if quad_tree[i][j] != number:                                        # 탐색한 위치의 숫자가 기준 숫자와 다르면
                print('(', end='')                                               # 4등분으로 나눈다. 즉 재귀함수 각 4분면에 맞게 4번 호출
                divideConquer(x, y, length//2)
                divideConquer(x, y+length//2, length//2)
                divideConquer(x+length//2, y, length//2)
                divideConquer(x+length//2, y+length//2, length//2)
                print(')', end='')
                return
                
    print(number, end='')                                                        # 모두 탐색했는데 모두 숫자가 같아서 통과된 경우 기준값을 출
        
divideConquer(0, 0, N)                                                           # 분할정복 시작