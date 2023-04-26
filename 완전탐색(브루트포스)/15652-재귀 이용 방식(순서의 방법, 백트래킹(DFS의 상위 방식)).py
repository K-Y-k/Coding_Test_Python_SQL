# 15650번에서 start를 같은 숫자는 오면 안되어 index+1이었지만
# 여기서의 문제는 같은 숫자까지는 허용하므로 start를 i번째로 오게한다.


def permutation(index, start):
    if index == M:
        print(" ".join(map(str, result)))
    else:
        for i in range(start, N+1):
            visited[i] = True
            result[index] = i
            permutation(index+1, i)
            visited[i] = False
            

N, M = map(int, input().split())
visited = [False] * (N+1)
result = [0] * M
permutation(0, 1)
