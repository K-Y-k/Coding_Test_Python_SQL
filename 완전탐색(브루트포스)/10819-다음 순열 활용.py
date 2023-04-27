# 수식을 이용하여 수학적인 방법으로 풀 수 도 있으나
# N의 범위가 3<= N <=8 밖에 되지 않아 브루트포스로 모두 조회해보는 방식으로 접근해서 풀어보려한다.

# 수의 순서만 변경할 수 있으므로 N x N! = 8 x 8! = 32만으로
# 1억에 1초 정도인데 그에 비해 정말 작은 수로 모든 경우를 다 해봐도 된다.

# 즉, 기존 다음 순열 원리를 활용하여 각 순열을 모두 조회하면서 그때의 순열에 따른 최대 차이 값을 갱신해가며 저장한다.


# 파이썬 전용 itertools의 permutations 모듈 활용 방식
# permutations에 숫자로 이루어진 배열(리스트)를 넣으면
# 해당 숫자 원소들의 모든 순열의 경우가 리스트로 담아져 이를 이용해 쉽게 작성할 수 있다.
from itertools import permutations     # 파이썬 전용 순열 라이브러리

N = int(input())                       # 순열 원소의 개수 입력
arr = list(map(int, input().split()))  # 순열 원소(숫자) 입력
permutation_list = permutations(arr)   # 모든 경우의 순열을 모두 저장된 리스트로 변환

result = 0                             # 최종 결과

for i in permutation_list:             # 모든 순열 리스트를 하나씩 조회하면서 
    temp = 0                           # 각 순열에 따른 차이의 결과 값 선언
    
    for j in range(N-1):               # 현재 순열에 수식 적용하여 합산
        temp += abs(i[j] - i[j+1])
    
    result = max(result, temp)         # 기존 저장된 최종 결과 최대 값과 현재 순열에서의 차이 값과 비교해서 가장 큰 값을 최종 결과에 갱신한다.
    
print(result)                          # 모든 반복을 조회한 후 저장된 최대 차이 값 출력



# 내가 직접 다음 순열 함수를 만들어서 활용 방식
# 다음 순열 문제에서 직접 함수를 만들어서 적용한다.
# 여기서 주의점은 같은 숫자가 올 수도 있으므로
# while i > 0 and current_permutation[i-1] >= current_permutation[i] 부분과
# while current_permutation[i-1] >= current_permutation[j] 부분에
# =의 부호도 같이 들어가야 한다!
def next_permutation(current_permutation):
    # 각 루프를 위한 현재 순열의 마지막 index까지 초기화
    i = len(current_permutation)-1
    j = len(current_permutation)-1
    k = len(current_permutation)-1
    
    # 1. i가 0보다 크고 현재 순열[i-1] < 현재 순열[i]를 만족하는 가장 큰 i를 찾는다.
    while i > 0 and current_permutation[i-1] >= current_permutation[i]:
        i -= 1
    # 1-2. 만약 못찾아서 i가 0이면 내림차순으로 마지막 순열이 온 것이므로 다음 순열은 없으므로 False 반환
    if i <= 0:
        return False

    # 2. j >= i이면서 현재 순열[i-1] < 현재 순열[j]를 만족하는 가장 큰 j를 찾는다.
    while current_permutation[i-1] >= current_permutation[j]:
        j -= 1

    # 3. 찾은 j의 위치 값과 i-1의 위치 값을 교환(swap)한다.        
    current_permutation[i-1], current_permutation[j] = current_permutation[j], current_permutation[i-1]
    
    # 위에서 찾았던 i위치부터 끝까지 뒤집는다.
    while i < k:
        current_permutation[i], current_permutation[k] = current_permutation[k], current_permutation[i]
        i += 1
        k -= 1
    # 다음 순열이 있으므로 True로 반환    
    return True

def calculate(current_permutation):                         # 비교 값에 합산 및 최대 값 적용 함수 선언
    global result                                           # 최종 최대 차이 결과 값을 가져옴
    temp = 0                                                # 현재 순열에 따른 차이의 결과 값 선언
    
    for i in range(len(current_permutation)-1):             # 현재 순열에 문제에 주어진 수식을 적용하여 합산
        temp += abs(current_permutation[i] - current_permutation[i+1])
    
    result = max(result, temp)                              # 기존 저장된 최종 결과 최대 값과 현재 순열에서의 차이 값과 비교해서 가장 큰 값을 최종 결과에 갱신하고 반환
    return result


N = int(input())
permutation_list = list(map(int, input().split()))
result = 0

permutation_list.sort()

while True:
    result = calculate(permutation_list)                    # 현재 순열에 비교 값에 합산 및 최대 값 적용 함수로 최종 결과 최대 값 갱신
    
    if not next_permutation(permutation_list):              # 만약 False이면 마지막 순열이므로 
        break                                               # 반복 종료
        
print(result)                                               # 모든 반복을 조회한 후 저장된 최대 차이 값 출력
