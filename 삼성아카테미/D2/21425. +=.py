# A와 B의 크기에 따라 증가 연산을 해주면서
# A와 B가 N이 초과 될 때까지 진행해준다.

T = int(input())

for test_case in range(1, T+1):
    A, B, N = map(int, input().split())

    count = 0

    while True:
        if A > N or B > N:                  # A와 B가 N이 초과 될 때까지 진행해준다.
            break

        if A > B:                           # A와 B의 크기에 따라 증가 연산을 해준다.
            B += A
        else:
            A += B

        count += 1


    print(count)
