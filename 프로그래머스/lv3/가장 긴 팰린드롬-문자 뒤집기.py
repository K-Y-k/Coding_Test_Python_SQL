# 처음에 내가 시도한 방식은 받아온 문자를 처음부터 거꾸로 뒤집은 값을 지정한 후
# 각 인덱스 루프에 따른 주어진 문자와 뒤집은 문자의 인덱스를 비교했지만
# 이건 인덱스 위치에 따른 문제가 있어 불가능하다.
def solution(s):
    answer = 0
    a = s[::-1]                               # 각 인덱스 루프에 따른 주어진 문자와 뒤집은 문자의 인덱스를 비교했지만

    for i in range(len(s)):
        for j in range(i+1, len(s)+1): 
            if s[i:j] == a[i:j]:              # 이건 인덱스 위치에 따른 문제가 있어 불가능하다.
                if answer < len(s[i:j]):
                    answer = len(s[i:j])
                    

    return answer



# 슬라이싱으로 받아온 인덱스의 문자에서 뒤집은 문자를 비교해야한다.

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:          # 슬라이싱으로 받아온 인덱스의 문자에서 뒤집은 문자를 비교해야한다.
                if answer < len(s[i:j]):
                    answer = len(s[i:j])
                    

    return answer