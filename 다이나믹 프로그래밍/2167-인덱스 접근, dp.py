# 내가 푼 방식
# 입력한 정수들을 리스트에 넣은 후
# K번 만큼 (i, j)에서 (x, y)까지의 값들을 루프로 조회해서 누적합산 시켰다.
# 하지만 문제의 주어지는 좌표 최대 범위가 넓어 시간초과가 발생한다.

N, M = map(int, input().split())
matrix = [(list(map(int, input().split()))) for _ in range(N)]

K = int(input())

for _ in range(K):
    total = 0
    i, j, x, y = map(int, input().split())

    for k in range(i-1, x):
        for l in range(j-1, y):
            total += matrix[k][l]

    print(total)



# DP를 활용한 방식
# 솔직히 이렇게까지 패턴을 생각하며 세우기는 어려움..
    
N, M = map(int, input().split())
matrix = [(list(map(int, input().split()))) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

K = int(input())

for a in range(1, N+1):
    for b in range(1, M+1):
        # 현재 위치의 넓이를 제외한 이전 넓이를 구하기 위한 점화식이다.
        # 현재 위치에 x값(dp[a-1][b]), y값(dp[a][b-1]) 한칸씩 이전하기 전의 넓이를 합한 후 공통된 부분(dp[a-1][b-1])을 빼주었다.

        # 점화식 적용 후 현재 위치의 값(matrix[a-1][b-1])을 더해준다.
        dp[a][b] = (dp[a-1][b] + dp[a][b-1] - dp[a-1][b-1]) + matrix[a-1][b-1]


for _ in range(K):
    i, j, x, y = map(int, input().split())

    # 위에 현재 위치에 따른 이전 위치들을 합한 넓이를 모두 적용해놨기에
    # 최대 크기의 넓이(dp[x][y])에서 포함되지 않는 이전 넓이들(dp[i-1][y], dp[x][j-1])을 제거해주고
    # 제거하면서 2번 중복 제거한 부분(dp[i-1][j-1])을 다시 더해준다.
    print((dp[x][y] - dp[i-1][y] - dp[x][j-1]) + dp[i-1][j-1])
