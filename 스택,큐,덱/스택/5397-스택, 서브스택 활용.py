# 화살표로 왼쪽으로 이동하면 이동할 때의 문자를 서브 스택에 넣어주고
# 화살표로 오른쪽으로 이동하면 서브 스택의 문자를 다시 꺼내서 넣어준다.
# 주의점은 모두 입력하고 왼쪽으로 이동해놓기만한 경우가 있을 수 있으므로
# 마지막에 서브 스택의 값들도 모두 꺼내는 작업을 하고 이어 붙여줘야한다.

N = int(input())

for _ in range(N):
    stack = []
    cursor_sub = []

    command = list(input())

    for i in command:
        if i == '<':                            # 화살표로 왼쪽으로 이동하면
            if stack:
                cursor_sub.append(stack.pop())  # 이동할 때의 문자를 서브 스택에 넣어주고

        elif i == '>':                          # 화살표로 오른쪽으로 이동하면
            if cursor_sub:
                stack.append(cursor_sub.pop())  # 서브 스택의 문자를 다시 꺼내서 넣어준다.
        elif i == '-':
            if stack:
                stack.pop()
        else:
            stack.append(i)

    a = ''.join(stack)
    b = ''.join(cursor_sub[::-1])               # 모두 입력하고 왼쪽으로 이동해놓기만한 경우가 있을 수 있으므로 마지막에 서브 스택의 값들도 모두 꺼내는 작업을 하고 이어 붙여줘야한다.

    print(a+b)