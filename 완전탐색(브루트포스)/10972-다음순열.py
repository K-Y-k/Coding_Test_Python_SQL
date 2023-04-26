# 다음 순열을 구하는 패턴은 이와 같다.
# 1. i >= 0이면서 현재 순열[i-1] < 현재 순열[i]를 만족하는 가장 큰 i를 찾는다. ex) 5 3 / 4 1 2 일 때 3이 i-1이고 4가 i이다.
# 1-2. 만약 못찾아서 i가 0이면 내림차순으로 마지막 수열이 온 것이므로 다음 순열은 없다. ex) 5 4 3 2 1
# 2. j >= i이면서 현재 순열[i-1] < 현재 순열[j]를 만족하는 가장 큰 j를 찾는다.
# 3. 찾은 j의 위치 값과 i-1의 위치 값을 교환(swap)한다.
# 4. 현재순열[i]위치부터 끝까지 뒤집는다.

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


N = int(input())                                          # 순열 개수 입력
current_permutation = list(map(int, input().split()))     # 현재 순열을 입력

if next_permutation(current_permutation):                 # True로 반환된 경우 
    print(' '.join(map(str, current_permutation)))        # 다음 순열을 출력
else:                                                     # False로 반환된 경우 마지막 순열이므로
    print(-1)                                             # -1로 출력