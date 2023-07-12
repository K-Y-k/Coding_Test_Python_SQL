# 내가 푼 방식
# 문자열을 쪼개고 나서
# 연산대상1, 연산자, 연산대상2, 정답 부분을 각자 따와서 
# 연산을 한 것이 정답이 맞는지 틀린지를 결과에 넣어준다.

def solution(quiz):
    result = []

    for i in quiz:
        s = i.split(' ')              # 문자열을 쪼개고 나서

        a = int(s[0])                 # 연산대상1

        if s[1] == '-':               # 연산자, 연산대상2
            b = -int(s[2])
        else:
            b = int(s[2])

        answer = int(s[-1])           # 정답 부분을 각자 따와서

        if a + b == answer:           # 연산을 한 것이 정답이 맞는지 틀린지를 결과에 넣어준다.
            result.append('O')
        else:
            result.append('X')


    return result