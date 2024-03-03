# 문제에서 현재 값부터 큰 값중 가장 작은 소수를 찾으라고 했으므로
# 현재 입력 값부터 무한 반복문으로 1씩 증가시켜가며 소수를 판별해갔다. 

T = int(input())

def is_prime(n):
    if n < 2 :                     # 2보다 작으면 소수가 아니므로 False 반환
        return False

    i = 2

    while i * i <= n:              # 2부터 i*i까지 반복
        if n % i == 0:             # 만약 나누어 떨어지면 소수가 아니므로 False 반환
            return False

        i += 1

    return True                    # 위 과정을 거치고 통과하면 소수이므로 True 반환


for _ in range(T):
    number = int(input())          # 현재 입력 값부터
 
    while True:                    # 무한 반복문으로
        if is_prime(number):       # 소수이면
            print(number)          # 현재 값을 출력하고
            break                  # 무한 반복문 종료

        number += 1                # 소수가 아니면 1씩 증가시켜 다음 소수 판별을 이어가게 했다.
