N = int(input())                                          # 우리 세로 칸의 값 입력
mod = 9901                                                # 나눠야하는 값을 변수로 저장

d = [[0]*3 for _ in range(N+1)]                           # 초기화
d[0][0] = 1                                               # 아무 것도 배치하지 않았을 때에도 경우의 수 포함이라고 했으므로 1로 초기화

for i in range(1, N+1) :                                  # 1부터 입력한 우리 칸 길이까지 반복
    # 점화식에 for문에서 값을 구하는 도중 메모리 초과 가능성이 있어 % 9901도 해준다.
    d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % mod   # 배치하지 않았을 때
    d[i][1] = (d[i-1][0] + d[i-1][2]) % mod               # 왼쪽에 배치했을 때
    d[i][2] = (d[i-1][0] + d[i-1][1]) % mod               # 오른쪽에 배치했을 때
        
print(sum(d[N]) % mod)                                    # 최종 경우의 수의 각 케이스의 합 9901의 나머지를 출력
