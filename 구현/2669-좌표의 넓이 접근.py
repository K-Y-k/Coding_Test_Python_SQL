# 점 좌표가 주어진 넓이를 점 좌표가 아닌, 박스 좌표라고 생각하기
# 예시로 (0,0)부터 (1,1)까지이면 넓이가 1인 박스 좌표라고 생각한다.

# 그렇기에 박스는 점보다 input() 값이 1개 더 필요하다.
# i, j가 주어지면, range(i, j+1) 범위가 아닌, range(i, j + 1 - 1)
# 즉 range(i, j) 범위를 순회해야한다.

matrix = [[0]*100 for _ in range(100)]

answer = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):       # range(y1, y2+1)이 아닌 이유는 좌표가 아니라 박스를 구해야 해서
        for j in range(x1, x2):
            if matrix[i][j] == 0: # 아직 0이면
                matrix[i][j] = 1  # 1로 갱신해줘 중복 카운팅이 안되게 하고
                answer += 1       # 총 넓이에 카운팅


print(answer)