# 입력한 단어를 5행에 맞춰 리스트에 넣고
# 리스트를 조회해서 단어의 길이의 최대 길이를 찾고
# 세로로 읽으면서 답에 넣는다.
# 주의점은 단어의 가로 라인은 길이가 다 다르기에 가로 길이 조건을 설정해야한다.

T = int(input())

for test_case in range(1, T + 1):
    word_li = []
    answer = ''
    
    for _ in range(5):
        word_li.append(str(input()))
        
    max_len = 0
    for i in range(5):
        max_len = max(max_len, len(word_li[i]))
    
    
    for i in range(max_len):
        for j in range(5):
            if i < len(word_li[j]):               # 주의점은 단어의 가로 라인은 길이가 다 다르기에 가로 길이 조건을 설정해야한다.
                answer += word_li[j][i]
        
        
    print('#' + str(test_case), answer)