# 다음 순열을 구하는 패턴과 같지만
# 이전 순열이므로 i위치와 j위치의 값을 가장 작은 것을 찾는 것으로 부등호를 바꿔준다.

# PS) 만약 같은 수가 들어갈 수 있는 비내림차순의 경우의 문제라면
# 1. 현재 순열[i-1] >= 현재 순열[i]
# 2. 현재 순열[i-1] >= 현재 순열[j]로 부등호 =도 같이 처리해야한다.


def next_permutation(current_permutation):
    i = len(current_permutation)-1
    j = len(current_permutation)-1
    k = len(current_permutation)-1
    
    while i > 0 and current_permutation[i-1] < current_permutation[i]: # 부등호 변경해야하는 부분
        i -= 1

    if i <= 0:
        return False
    
    while current_permutation[i-1] < current_permutation[j]:           # 부등호 변경해야하는 부분
        j -= 1

    current_permutation[i-1], current_permutation[j] = current_permutation[j], current_permutation[i-1]

    while i < k:
        current_permutation[i], current_permutation[k] = current_permutation[k], current_permutation[i]
        i += 1
        k -= 1
    return True


N = int(input())                                          
current_permutation = list(map(int, input().split()))     

if next_permutation(current_permutation):                 
    print(' '.join(map(str, current_permutation)))        
else:                                                     
    print(-1)                                            