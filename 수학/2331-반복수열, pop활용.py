A, P = map(int, input().split())                # 초기값 A, 제곱할 값 P

P_checkList = [A]                               # 첫번째 A 값을 미리 넣고 초기화

while True:                                  
    next_P = 0
    for i in str(P_checkList[-1]):              # 배열변수[-1]은 마지막 원소를 가져오고 int형인 숫자를 str로 변환하고 각 자릿수의 값을 꺼내와사
        next_P += int(i)**P                     # 각 자리숫를 P제곱한 것을 더해준다. 
        
    if next_P in P_checkList:                   # 각 자릿수에 P제곱을 더한 값이 P리스트 안에 있으면 반복 수열이 시작됐다는 뜻이므로
        while True:                             # 무한 반복으로
            if next_P == P_checkList.pop():     # pop으로 반복되는 부분을 순차적으로 다 꺼내고 첫번째 반복 시작 값과 같아지면 반복구간이 끝난 것이므로
                print(len(P_checkList))         # 반복되지 않은 값들의 개수만 출력하게 되고
                exit()                          # 종료시킨다.

    else:                                       # P리스트에 없으면 새로운 값이므로
        P_checkList.append(next_P)              # 넣어준다.