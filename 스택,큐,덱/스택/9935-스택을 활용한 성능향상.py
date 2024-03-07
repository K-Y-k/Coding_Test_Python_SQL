# 내가 푼 방식 => 시간초과 발생
# replace는 처음부터 끝까지 모든 문자를 스캔해야하므로 최악의 경우 시간 복잡도가 O(n⋅m)이 된다.

word = input()
boom_word = input()

while True:
    if boom_word in word:
        word = word.replace(boom_word, '')
    else:
        break

if word == '':
    print('FRULA')
else:
    print(word)



# 스택으로 시간초과 해결한 방식 
# 스택을 활용해서 시간복잡도가 O(1)
# 단어를 하나씩 스택에 담아가면서 담고나서 폭발문자의 길이만큼 빼온 문자가 폭발 문자와 동일하다면
# 스택에서 빼온 길이만큼 반복해서 지워준다. 
    
import sys

word = list(sys.stdin.readline().strip())
boom_word = list(sys.stdin.readline().strip())

N = len(boom_word)

stack = []

for i in word:                                   
    stack.append(i)                                # 단어를 하나씩 스택에 담아가면서

    if stack[-N:] == boom_word:                    # 담고나서 폭발문자의 길이만큼 빼온 문자가 폭발 문자와 동일하다면
        for _ in range(N):                         # 스택에서 빼온 길이만큼 반복해서 지워준다. 
            stack.pop()


answer = ''.join(map(str, stack))

if answer == '':
    print('FRULA')
else:
    print(answer)
