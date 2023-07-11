# 내가 푼 방식
# 2차원 배열의 각 요소와 입력한 아이디, 비밀번호를 비교하여
# 아이디, 비밀번호 둘 다 같으면 정답에 login을 넣었고
# 아이디만 맞았을 경우 boolean이라는 구분자 변수에 1로 변경하여
# 모두 조회하고 정답에 login이 없고 빈 문자열이면
# boolean 구분자 변수를 확인하고 해당 값의 결과를 넣었다.  

def solution(id_pw, db):
    answer = ''
    boolean = 0
    
    for i in db:                                    # 2차원 배열의 각 요소와 입력한 아이디, 비밀번호를 비교하여
        if i[0] == id_pw[0] and i[1] == id_pw[1]:   # 아이디, 비밀번호 둘 다 같으면 정답에 login을 넣었고
            answer = 'login'
        elif i[0] == id_pw[0] and i[1] != id_pw[1]: # 아이디만 맞았을 경우 boolean이라는 구분자 변수에 1로 변경하여
            boolean = 1
            
    if answer == '':                                # 모두 조회하고 정답에 login이 없고 빈 문자열이면
        if boolean == 0:                            # boolean 구분자 변수를 확인하고 해당 값의 결과를 넣었다.
            answer = 'fail'
        else:
            answer = 'wrong pw'
    
    
    return answer



# 좀더 정돈된 방식
# 정답의 첫 초기 값을 둘 다 틀린 결과로 넣어
# 조회하면서 아이디, 비밀번호 둘 다 맞았을 때와 아이디만 맞았을 때의 결과를 넣었다.
# 하지만 둘 다 맞았을 때는 더 이상 진행될 필요가 없고 더 조회하다가 정답에 결과가 바뀔 수 있으므로 바로 반환하게 하였다. 

def solution(id_pw, db):
    answer = 'fail'                                  # 정답의 첫 초기 값을 둘 다 틀린 결과로 넣어
    
    for i in db:
        if i[0] == id_pw[0] and i[1] == id_pw[1]:    # 조회하면서 아이디, 비밀번호 둘 다 맞았을 때와 아이디만 맞았을 때의 결과를 넣었다.
            answer = 'login'
            return answer                            # 하지만 둘 다 맞았을 때는 더 이상 진행될 필요가 없고 더 조회하다가 정답에 결과가 바뀔 수 있으므로 바로 반환하게 하였다. 
        elif i[0] == id_pw[0] and i[1] != id_pw[1]:
            answer = 'wrong pw'
            

    return answer