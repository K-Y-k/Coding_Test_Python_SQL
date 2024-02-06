# 후위 연산식은 숫자는 스택에 넣고
# 연산자를 만나면 최근 숫자 2개를 꺼내서 계산한 후 다시 스택에 넣는다.

# 주의점은 스택은 끝에서부터 꺼내는데
# 계산할 때 -, /는 순서에 따라 결과가 다르므로 두번째 꺼낸 값이 앞에 와야한다!

N = int(input())

postFix = list(input())
stack = []

# 방식 1) 배열에 적용 
num = [0]*N
for i in range(N):                            # 피연산자에 적용할 숫자 입력
    num[i] = int(input())

# 방식 2) 딕셔너리에 적용
# num_dic = {}
# for i in range(N):  # 최대 생성될 수 있는 알파벳만큼 딕셔너리에 알팟벳-숫자를 매칭시켜놈
#     num_dic[chr(ord('A') + i)] = int(input()) # A부터 + N번째까지 알파벳과 숫자 적용


for i in postFix:
    if i.isalpha():
        stack.append(num[ord(i) - ord('A')])  # 방식 1) 적용했던 피연산자의 숫자를 가져와서 스택에 넣기
#       stack.append(num_dic[i])              # 방식 2)
    else:
        b = stack.pop()                       # 계산할 때 -, /는 순서에 따라 결과가 다르므로 두번째 꺼낸 값이 앞에 와야한다!
        a = stack.pop()

        if i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)
        elif i == '+':
            stack.append(a + b)
        else:
            stack.append(a - b)

print('%.2f' %stack[0])
