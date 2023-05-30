# 1.현재 큐에서 하나를 꺼낼 때 현재 큐 전체를 조회해서 
# 2.꺼낸 값보다 큰 값(=우선순위)이 있을 경우 다시 뒤에 넣고
# 3.any는 모두 조회했을 때 모두 False인 경우 False이므로 
#   즉, 위 조건이 모두 적용되지 않아 else연산으로 진행하여 turn을 1 상승시키고
# 4.만약 현재 꺼내온 인덱스가 입력한 원하는 location 값일 경우 쌓아왔던 turn의 값으로 return


def solution(priorities, location):
    answer = 0
    
    printer = []
    for i, p in enumerate(priorities):           # 각 원소의 위치(i)와 우선순위 값(p)을 같이 튜플 쌍으로 묵어서 넣는다.
        printer.append((i,p))
    
    turn = 0                                     # 현재까지 출력된 값 선언 및 초기화
    while printer:                               # 큐가 빌 때까지 반복
        x = printer.pop(0)                       # 제일 앞에 하나를 꺼내고
        
        
        if any(x[1] < y[1] for y in printer):    # 꺼낸 값이 큐안에 있는 우선순위 값보다 작을 경우는 
            printer.append(x)                    # 다시 뒤에 넣고

        else:                                    # 위 조건이 모두 안되어 결국 꺼낸 값이 우선순위가 제일 큰 경우
            turn += 1                            # 현재까지 출력된 값을 +1해주고
            
            if x[0] == location:                 # 만약 현재 꺼낸 인덱스가 문제에서 입력한 location과 동일한 경우 
                break                            # 이 값을 원한 것이므로 반복을 종료
    
    answer = turn                                # 현재까지 출력된 값을 넣고 반환
    return answer