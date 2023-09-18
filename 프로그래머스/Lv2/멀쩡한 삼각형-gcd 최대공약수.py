# 일정한 패턴이 있을거라고 생각해서 찾아봤지만 내 힘으로 찾을 수 없었다..
# 최대공약수와 관계가 있었고
# 대각선을 그을 때 점을 지나는 개수가 최대공약수의 개수였고
# W + H - 최대공약수 = 사각형으로 만들 수 없는 블록의 개수로
# 최종 결과식은 모든 블록(W * H)에서 사각형으로 만들수 없는 블록들(W + H - 최대공약수)을 뺀 것이다.

import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def solution(w,h):
    answer = 0
    
    gcd_ = gcd(w, h)                        # 대각선을 그을 때 점을 지나는 개수가 최대공약수의 개수였고 W + H - 최대공약수가 사각형으로 만들 수 없는 블록의 개수였다.
    
    answer = w * h - (w + h - gcd_)         # 최종 결과식은 모든 블록(W * H)에서 사각형으로 만들수 없는 블록들(W + H - 최대공약수)을 뺀 것이다.
    
    return answer

    # return  w*h - (w+h-math.gcd(w,h))