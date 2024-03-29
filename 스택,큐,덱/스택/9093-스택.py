import sys
input = sys.stdin.readline

t = int(input())                                     # 입력 줄 개수 선언
for _ in range(t):                                   # 입력 줄 만큼 반복
    s = input()                                      # 단어 입력
    stack = []                                       # 스택 선언

    for ch in s:                                     # 입력한 단어들 조회
        if ch == ' ' or ch == '\n':                  # 공백이나 개행이 있을 경우 
            print(''.join(stack[::-1]), end='')      # 역순으로 출력, 리스트 요소별로 공백을 삽입해 join()함
                                                     # array[start : end : step] 슬라이스 구조(리스트, 튜플, 문자열 등 연속적인 객체의 범위를 지정해 객체를 가져오는 방법)
            stack.clear()
            print(ch, end='')
        else:                                        # 단어가 있는 경우
            stack.append(ch)                         # 스택에 넣기