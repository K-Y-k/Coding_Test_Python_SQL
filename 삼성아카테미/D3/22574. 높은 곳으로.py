# 내가 푼 방식 - 일부 테케만 맞음
# N번째까지의 층을 더해간다고 했으므로 N번까지 순차적으로 층을 더해가는데
# 더해가면서의 층이 P층에서로 멈추면 터지므로 이때는 넘어가는 형태로 진행했지만
# 결국 최상층에 도달하는 방식이 아니었음

T = int(input())

for test_case in range(1, T+1):
    N, P = map(int, input().split())
    level = 0

    for i in range(1, N+1):
        if level + i == P:
            continue
        else:
            level += i

    print(level)



# P층에 도달하면 멈추면 안되므로
# P-1층까지는 무조건 도달할 수 있어서
# N번까지 순차적으로 더할 때 P층에 도달하면 -1을 처리해주면서 진행하면 최상층에 도달할 수 있다.

T = int(input())

for test_case in range(1, T+1):
    N, P = map(int, input().split())
    level = 0

    for i in range(1, N+1):
        level += i

        if level == P:
            level -= 1

    print(level)
