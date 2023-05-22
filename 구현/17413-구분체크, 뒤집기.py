# < > 안에 있는 것은 바뀌지 않고 그외는 공백 기준으로 된 단어들이 뒤집어진다.

# 즉, < > 안에 있을 때는 체크 값을 True로 하여 구분 적용하고
# 아닌 경우의 단어는 현재 넣는 문자 + 담아두었던 임시 공간의 문자열로 거꾸로 넣는 형태로 나타낼 수 있다.



S = input()                        # 문자 입력

check = False                      # < >안에 있는 상태인지 체크하기 위해 선언, 초기 값은 False
temp = ''                          # 빈 값의 담을 공간 선언
result = ''                        # 최종 답을 넣을 공간 선언

for i in S:                        # 입력했던 문자를 하나씩 조회
    if check == False:             # False인 상태일 때
        if i == '<':               # <이 오면 
            check = True           # True로 바꾸고
            temp += '<'            # <를 담아둔다.

        elif i == ' ':             # 공백이면
            temp += ' '            # 공백을 추가한
            result += temp         # 임시 저장한 값을 최종 결과에 넣고
            temp = ''              # 임시 저장 값을 초기화

        else:                      # 일반 단어이면
            temp = i + temp        # 거꾸로 담는다.
            
    elif check == True:            # True인 상태는 <>안에 있는 단어이므로
        if i == '>':               # >이 오면
            check = False          # False로 바꾸고
            temp += '>'            # >을 추가한
            result += temp         # 임시 저장한 값을 최종 결과에 넣고
            temp = ''              # 임시 저장 값을 초기화

        else:                      # 아직 단어가 오는 상태이면
            temp += i              # < > 안에 있는 단어이므로 그대로 임시 저장 공간에 넣는다.
        
        
print(result + temp)               # +temp를 넣은 것은 마지막 단어 다음에는 공백이 안와서 해당 임시 저장된 상태를 넣지 못한 상태라서 처리해준 것
