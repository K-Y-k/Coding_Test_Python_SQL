# 이 문제에서는 15649번과는 달리 중복이 가능하므로 방문에 대한 처리를 할 필요가 없어져 방문처리 관련 부분만 지워주면 된다.

def permutation(index):
    if index == M:
        print(" ".join(map(str, result)))
        return
    else:
        for i in range(1, N+1):
            result[index] = i
            permutation(index+1)

N, M = map(int, input().split())
result = [0] * M
permutation(0)