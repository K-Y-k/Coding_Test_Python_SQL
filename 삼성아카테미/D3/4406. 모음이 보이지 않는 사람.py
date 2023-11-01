# 모음 리스트를 따로 선언하고
# 받아온 문자열에서 문자 하나씩 조회하며 모음 리스트에 포함되어 있지 않으면 자음이므로 정답에 새로 넣기

T = int(input())

for test_case in range(1, T + 1):
    dic = ['a', 'e', 'i', 'o', 'u']
    
    word = str(input())
    answer = ''
    
    for i in word:
        if i not in dic:
            answer += i
            
    print('#' + str(test_case), answer)