# 단순 gcd 구현 방식
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    boonja = numer1 * denom2 + numer2 * denom1         # 분자
    boonmo = denom1 * denom2                           # 분모
    
    maximum_value = 1                                  # 나눠질 수 있는 최대 값 선정하기 위해 선언
    for i in range(2, min(boonja, boonmo)):            # 분모, 분자 중 작은 값까지 나눠질 수 있으니 범위를 min까지로 조정
        if boonja % i == 0 and boonmo % i == 0:        # 분모 분자 둘 다 나눠지는 경우
            maximum_value = i                          # 나눠질 수 있는 값에 갱신

    if boonja//maximum_value != boonmo//maximum_value: # 분모, 분자가 서로 다른 경우
        answer.append(boonja//maximum_value)           # 각 나눠질 수 있는 값으로 나누고 넣는다.
        answer.append(boonmo//maximum_value)
    else:                                              # 분모, 분자가 서로 같은 경우는 [1, 1]이므로 따로 넣어줌
        answer.append(1) 
        answer.append(1)
    
    return answer



# 최적화 gcd함수 활용 방식
def gcd(a, b):                                         # gcd함수
    if b == 0:                                         # 0으로 나누어 떨어지지 않을 때
        return a                                       # 반환
    else:                                              # 나누어 떨어지는 경우면 
        return gcd(b, a%b)                             # 재귀 반환
    
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2
    
    gcd_value = gcd(boonmo, boonja)                    # gcd 함수로 최대 공약수 반환
    answer.append(boonja/gcd_value)
    answer.append(boonmo/gcd_value)
    
    return answer



# math 라이브러리 활용
import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2
    
    gcd_value = math.gcd(boonmo, boonja)               # math의 gcd 함수로 최대 공약수 반환
    answer.append(boonja/gcd_value)
    answer.append(boonmo/gcd_value)
    
    return answer
