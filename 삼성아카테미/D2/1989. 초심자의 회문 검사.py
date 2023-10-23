T = int(input())

for test_case in range(1, T + 1):
    word = str(input())
    reverse_word = ''
    answer = 0
    
    for i in reversed(word):
        reverse_word += i
    
    if word == reverse_word:
        answer = 1
    
    print('#' + str(test_case), answer)