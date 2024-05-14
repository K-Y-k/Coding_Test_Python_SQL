# 내가 푼 방식 - 일붙 테케 실패
# 무한 루프를 돌리면서 현재의 암호의 각자리를 조회하면서 현재 위치의 뒤의 값과 동일하면
# 현재 위치와 뒤 위치의 값만 제외한 슬라이싱으로 담는 방식으로
# 위 조건을 한번도 거치지 않고 모두 조회한 경우 무한루프를 종료했다.

N, password = map(int, input().split())
password = str(password)

while True:
    for i, val in enumerate(password):
        if i < N-1 and password[i] == password[i+1]:
            password = password[:i] + password[i+2:]
            N -= 2
            break
    else:
        break


print(password)



# 스택 활용 방식
# 암호를 하나씩 조회하면서
# 스택이 비어있거나 스택의 최근 값과 현재 암호의 값이 다른 경우는 스택에 넣고
# 스택의 최근 값과 현재 암호 값이 같은 경우는 스택의 최근 값을 빼준다.

N, password = map(int, input().split())
answer_password = []

password_li = []
for i in str(password):
    password_li.append(int(i))

for i in password_li:                                           # 암호를 하나씩 조회하면서
    if len(answer_password) == 0 or answer_password[-1] != i:   # 스택이 비어있거나 스택의 최근 값과 현재 암호의 값이 다른 경우는
        answer_password.append(i)                               # 스택에 넣고
    else:                                                       # 스택의 최근 값과 현재 암호 값이 같은 경우는
        answer_password.pop()                                   # 스택의 최근 값을 빼준다.

print(answer_password)

