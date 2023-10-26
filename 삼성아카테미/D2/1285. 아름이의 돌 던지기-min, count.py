T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    rock_li = list(map(int, input().split()))
    result = []

    for i in range(N):
        result.append(abs(rock_li[i]))

    m = min(result)

    print('#' + (test_case), m, result.count(m))