# for문의 reversed로 거꾸로 출력한 것을 저장하고
# 비교하여 결과 출력  

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