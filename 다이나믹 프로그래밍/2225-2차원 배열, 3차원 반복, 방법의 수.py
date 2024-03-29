mod = 1000000000                          # 문제에서 나누라는 수를 변수로 선언

N, K = map(int, input().split())          # 숫자, 개수 입력 값 선언

d = [[0]*(N+1) for _ in range(K+1)]       # 각 개수의 숫자들만큼 초기화

d[0][0] = 1                               # K가 1개이면 자기자신 1개만 가능하여 1로 초기화

for i in range(1, K+1) :                  # K 개수만큼 반복
    for j in range(0, N+1) :              # 문제에서 N의 범위가 0부터 N까지이므로
        for l in range(0, j+1) :          # L의 모든 경우의 수 넣기
            d[i][j] += d[i-1][j-l]        # 점화식
        d[i][j] %= mod                    # 문제에서 나누어주라고 함
        
print(d[K][N])                            # 모든 방법의 수 출력