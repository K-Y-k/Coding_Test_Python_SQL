# 내가 푼 방식
# 최대공약수를 구하는 함수를 구현하였고
# 최소공배수를 구하는 공식을 이용해서 구했다.


def solution(n, m):
    answer = []
    
    g = gcd(n,m)       
    answer.append(g)
    
    a = n*m//g         # 최소공배수를 구하는 공식 : a x b // 최대공약수
    answer.append(a)
    
    
    return answer


def gcd(a, b):         # 최대공약수를 구하는 함수
    if b == 0:
        return a
    else:
        return gcd(b, a%b)