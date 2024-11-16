# 무한 루프로 0부터 N의 값 이상이 될 때까지 반복하여
# 세제곱근이 N이상으로 도달하게 적용해나간다.
# N보다 큰 수일 경우 세제곱이 될 수 없는 수이므로 -1로 적용

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    temp = 0
    x = 0

    while True:
        temp = x ** 3

        if temp >= N:
            if temp > N:
                x = -1
            break

        x += 1

    print('#' + str(test_case), x)