# 처음 오는 순열을 하나 출력한 후
# 무한 반복을 통해 다음 순열을 구하는 패턴을 이용해서 출력하면 된다.

# PS) 만약 같은 수가 들어갈 수 있는 비내림차순의 경우의 문제라면
# 1. 현재 순열[i-1] <= 현재 순열[i]
# 2. 현재 순열[i-1] <= 현재 순열[j]로 부등호 =도 같이 처리해야한다.


def next_permutation(current_permutation):
    # 각 루프를 위한 현재 순열의 마지막 index까지 초기화
    i = len(current_permutation)-1
    j = len(current_permutation)-1
    k = len(current_permutation)-1
    
    # 1. i >= 0이면서 현재 순열[i-1] < 현재 순열[i]를 만족하는 가장 큰 i를 찾는다.
    while i > 0 and current_permutation[i-1] > current_permutation[i]:
        i -= 1
    # 1-2. 만약 못찾아서 i가 0이면 내림차순으로 마지막 수열이 온 것이므로 다음 순열은 없으므로 False 반환
    if i <= 0:
        return False
    
    # 2. j >= i이면서 현재 순열[i-1] < 현재 순열[j]를 만족하는 가장 큰 j를 찾는다.
    while current_permutation[i-1] > current_permutation[j]:
        j -= 1

    # 3. 찾은 j의 위치 값과 i-1의 위치 값을 교환(swap)한다.
    current_permutation[i-1], current_permutation[j] = current_permutation[j], current_permutation[i-1]

    # 위에서 찾았던 i 위치부터 끝까지 뒤집는다.
    while i < k:
        current_permutation[i], current_permutation[k] = current_permutation[k], current_permutation[i]
        i += 1
        k -= 1
    # 다음 순열이 있으므로 True로 반환    
    return True


N = int(input())                                   # 순열의 개수 입력

current_permutation = []                           # 처음 오는 순열 초기화
for i in range(1, N+1):
    current_permutation.append(i)

while True:                                        # 무한 반복을 돌려
    print(' '.join(map(str, current_permutation))) # 현재 순열을 출력
    
    # 다음 순열이 있으면 다음 순열 값을 최신화하면서 무한반복이 진행되고
    if not next_permutation(current_permutation):  # 만약 다음 순열이 없으면 종료
        break