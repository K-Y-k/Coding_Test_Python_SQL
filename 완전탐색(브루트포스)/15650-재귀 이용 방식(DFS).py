# 오름차순이 추가되었으므로 for 루프가 1부터 현재 값이 아닌 모든 수가 아니고
# 현재 값보다는 큰 수부터인 모든 수로 변경해야하므로 start의 매개변수를 추가해 적용해주면된다.
# 또한 (1)문제에서는 중복되는 수가 올 수 있었기에 방문처리를 따로하여 백트래킹을 했지만
# 여기서는 현재 값에서 +1로 무조건 새로운 수가 나오므로 겹치지 않아 방문처리를 하지 않고 깊이탐색만 진행하면된다.


def permutation(index, start):                 # 매개변수에 start를 추가
    if index == M:
        print(' '.join(map(str, result)))
    else:
        for i in range(start, N+1):            # 현재 값보다는 큰 수가 나오게 하기 위해 start부터 조회
            result[index] = i
            permutation(index+1, i+1)          # start부분에 현재 값+1로 다음 깊이탐색에서는 큰 수부터 오게 갱신

N, M = map(int, input().split())
result = [0] * M

permutation(0, 1)