def is_prime(n) :                                     # 소수 확인 함수
    if n < 2 :                                        # 2보다 작으면 소수가 아니다(False)를 반환
        return False
    
    i = 2                                             # 초기 값 i를 2 선언
    while i*i <= n :                                  # 2부터 i*i까지 반복
        if n % i == 0:                                # 만약 나누어 떨어지면 소수가 아니다(False)를 반환
            return False
        i += 1    
        
    return True                                       # 위 과정을 거치면 소수이므로 True 반환 


N = int(input())                                      # 숫자 입력 개수 선언
prime_number = []                                     # 리스트 형태로 선언
prime_number = list(map(int, input().split()))        # 입력 개수만큼의 숫자들을 리스트로 형태로 넣음
cnt = 0                                               # 소수 개수 초기화

for i in prime_number :                               # 리스트 각 항 모두 순회
    if is_prime(i) :                                  # 각 항을 소수확인 함수 적용 하여 맞으면 소수개수(cnt)+1
        cnt += 1

print(cnt)                                            # 소수 개수 출력

