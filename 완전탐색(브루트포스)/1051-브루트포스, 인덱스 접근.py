# 사각형으로 주어진 각 값들이 
# 꼭지점인 값들만 동일하면 정사각형으로 인지하고
# 이 정사각형의 최대 넓이를 구하므로
# 하나씩 루프의 각 꼭지점 인덱스를 늘려가며 접근해야한다.
# 인덱스 범위를 잘 생각하며 구현해야했다.

N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]

answer = 1                                      # 최소값은 항상 1인 넓이이므로 1로 초기화

for i in range(N):
    for j in range(M):
        for k in range(1, M):                   # 1인 넓이는 초기화 했으므로 길이가 2부터 조회
            if i+k < N and j+k < M:
                if matrix[i][j] == matrix[i][j+k] and matrix[i][j] == matrix[i+k][j] and matrix[i][j] == matrix[i+k][j+k]:
                    answer = max(answer, (k+1)**2)

print(answer)