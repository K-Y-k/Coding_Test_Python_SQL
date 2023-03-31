# 내가 푼 insert del 함수 활용 방식 => 시간복잡도가 O(N)으로 시간초과 발생
import sys

word = list(input())
cursor = len(word)

N = int(input())


for _ in range(N):
    command_list = list(map(str, sys.stdin.readline().split()))
    
    if command_list[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif command_list[0] == 'D':
        if cursor != (len(word)-1):
            cursor += 1
    elif command_list[0] == 'B':
        if cursor != 0:
            del word[cursor-1]
    elif command_list[0] == 'P':
        word.insert(cursor, command_list[1])
        cursor += 1
        
result = ''
for i in word:
    result += i

print(result)




# 시간초과 해결한 방식 => 2개의 스택을 활용해서 시간복잡도가 O(1)인 append pop extend 함수 활용
import sys

word_stack1 = list(input())
word_stack2 = [] 

N = int(input())


for _ in range(N):
    command_list = list(map(str, sys.stdin.readline().split()))
    
    if command_list[0] == 'L':
        if word_stack1:
            word_stack2.append(word_stack1.pop())
    elif command_list[0] == 'D':
        if word_stack2:
            word_stack1.append(word_stack2.pop())
    elif command_list[0] == 'B':
        if word_stack1:
            word_stack1.pop()
    elif command_list[0] == 'P':
        word_stack1.append(command_list[1])
        
        
word_stack1.extend(reversed(word_stack2))
print(''.join(word_stack1))
    
print(word_stack1)