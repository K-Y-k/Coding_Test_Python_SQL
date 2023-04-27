from collections import deque

def solution(s, n):
    answer = ''
    
    upper_alphabet = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    
    lower_alphabet = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    
    
    index = 0
    
    for i in s:
        if i == ' ':
            answer += ' '
        elif i in upper_alphabet:
            index = upper_alphabet.index(i)
            upper_alphabet.rotate(-n)
            
            answer += upper_alphabet[index]
            upper_alphabet.rotate(n)
            
        elif i in lower_alphabet:
            index = lower_alphabet.index(i)
            lower_alphabet.rotate(-n)
            
            answer += lower_alphabet[index]       
            lower_alphabet.rotate(n)
    
    return answer