X = int(input())
line = 1                             # 줄은 1로 초기화 

while X > line:                      # 몇번째 줄(line)에 몇번째 위치(X)인지 파악
    X -= line
    line += 1

if line % 2 == 0:                    # 짝수 라인인 경우 부모가 1씩 늘어나고 분자가 1씩 줄어드므로
    a = X
    b = line - X + 1
    print(str(a) + '/' + str(b))
else:                                # 홀수 라인인 경우 분자가 1씩 늘어나고 부모가 1씩 줄어드므로
    a = line - X + 1
    b = X
    print(str(a) + '/' + str(b))