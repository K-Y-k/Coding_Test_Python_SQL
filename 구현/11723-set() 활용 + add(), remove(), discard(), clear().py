# 생각보다 주의해야할 점이 있었다.
# 1) 메모리 초과           : 일반 리스트로 활용할 시 연산의 수가 3백만까지라서 메모리가 부족하다.
#                           그래서 set()함수를 활용해야한다.
# 2) all과 empty 따로 처리 : 다른 연산은 연산과 숫자 2개가 입력되는데 all과 empty는 하나만 입력하기에
#                           처음 입력 저장을 map으로 각 입력 값 저장을 할 수 없다.
#                           split()으로 쪼갠 것을 하나의 변수에 담고 [0]항이 all과 empty일 경우 따로 처리

# discard()와 clear()
# set함수는 일반 리스트와 달리 discard()도 지원하는데 remove()랑 같은 삭제 처리이지만
# remove()는 해당 값이 없으면 에러가 발생하는데 discard()는 해당 값이 없으면 무시한다.
# 또한 clear()로 전부 비울 수 있다.



import sys

M = int(input())
S = set()

for _ in range(M):
    operation = sys.stdin.readline().split()
    
    if len(operation) == 1:                       # 쪼개진 데이터의 개수가 1개이면 all, empty중 하나이므로 따로 처리
        if operation[0] == "all":                 # all 연산
            S = set(range(1, 21))
        if operation[0] == "empty":               # 비우기 연산 
            S.clear()
    else:                                         # 쪼개진 데이터가 2개이면
        x = int(operation[1])                     # 연산에 들어갈 숫자를 선언
        
        if operation[0] == 'add':                 # 추가 연산
            S.add(x)
        elif operation[0] == 'remove':            # 삭제 연산
            S.discard(x)                          # remove()로 사용했다면 if x in S:로 조건처리를 해야했지만 discard는 없으면 생략함
        elif operation[0] == 'check':             # 체크 연산
            if x in S:
                print(1)
            else:
                print(0)
        elif operation[0] == 'toggle':            # 토글 연산
            if x in S:
                S.remove(x)
            else:
                S.add(x)