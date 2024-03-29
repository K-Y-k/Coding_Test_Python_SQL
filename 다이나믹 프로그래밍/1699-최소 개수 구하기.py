N = int(input())                      # 입력 값 선언

d = [0 for _ in range(N+1)]           # 점화식 배열 d는 입력한 값까지 0으로 초기화

for i in range(1, N+1) :              # 1~N까지 반복
    d[i] = i                          # 최소값을 구할 때는 초기값을 0으로 하면 안된다.
                                      # 또한 i일 때 i 값을 넘어갈 수 없다.
    for j in range(1, i+1) :          # 1~i까지 반복
        if j*j > i :                  # 만약 j^2이 i를 넘어가면 안되기에 반복을 그만
             break
        if d[i] > d[i-j*j] + 1 :      # d[i]이 d[i-j*j] + 1보다 크면 최소값을 구하므로 d[i-j*j] + 1을 넣는다.
            d[i] = d[i-j*j] + 1

print(d[N])                           # 최소값 출력