# 내가 푼 rotate()방식
from collections import deque

lower_word = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
upper_word = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

# rotate()연산은 다른 변수로 대입하려고 해도 기존껏도 적용되므로 따로 또 만듬
rot_lower_word = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
rot_upper_word = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

rot_lower_word.rotate(13)  
rot_upper_word.rotate(13)


result = ''

word = str(input())

for i in word:
    if i.islower():
        result += rot_lower_word[lower_word.index(i)]
    elif i.isupper():
        result += rot_upper_word[upper_word.index(i)]
    else:
        result += i
        
print(result)
    
        

# ascii 코드 변환 방식
word = input()

result = ''

for i in word:
    if i.isupper():
        if (65 <= ord(i) <= 77):
            result += chr(ord(i) + 13)   # A ~ M
        else:
            result += chr(ord(i) - 13)   # N ~ Z
    elif i.islower():
        if (97 <= ord(i) <= 109):
            result += chr(ord(i) + 13)   # a ~ m
        else:
            result += chr(ord(i) - 13)   # n ~ z
    else:
        result += i
        
print(result)