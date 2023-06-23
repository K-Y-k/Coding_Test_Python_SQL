# 뉴클리드 호제법으로 최대 공약수를 구하고
# 문제에서 제시된 숫자를 차례로 최소공배수를 구하면 주어진 숫자들에서의 공통의 최소공배수를 구할 수 있다. 


def solution(arr):
    answer = 1                                  # 첫 값과의 최소공배수를 확인하기 위해 1로 적용
    
    for i in arr:                               # 순차적으로 조회하며
        answer = answer * i // gcd(answer, i)   # 차례대로 최소 공배수를 적용해나가면 해당 숫자들이 포함된 공통의 최소 공배수가 된다.
        
    return answer


def gcd(a,b):                                   # 유클리드 호제법 : 최대 공약수 구하는 로직
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
        