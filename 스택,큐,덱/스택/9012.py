def valid(s):               # 함수로 선언
    count = 0               # 스택의 크기

    for ch in s:            # 모두 조회
        if ch == '(':       # (이면 스택 크기 증가
            count += 1   
        else:               # )이면 스택 크기 감소
            count -= 1   
 
        if count < 0:       # 여는괄호가 없고 닫는 괄호가 올 시 스택의 크기가 0보다 작아지므로 이때
            return 'NO'     # NO 반환

                            # 모두 조회한 후
    if count == 0:          # 스택의 크기가 0(스택이 비어있다)이면 모두 짝을 맞췄다는 뜻으로 YES 반환
        return 'YES'
    else:                   # 0이 아니면 (가 남아 있으므로 짝이 없어 NO반환
       return 'NO'

t = int(input())           # 입력 개수 선언
for _ in range(t):         # 입력 개수만큼 반복
    print(valid(input()))  # 함수 실행