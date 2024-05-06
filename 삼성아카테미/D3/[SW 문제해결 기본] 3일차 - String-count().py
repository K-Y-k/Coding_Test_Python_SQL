# 내가 푼 방식
# 키워드의 길이에 맞춰 각 단어의 위치에 따라 길이 만큼 슬라이싱한 단어를 찾는 단어와 일치할 때 카운팅했다.

T = 10

for test_case in range(1, T + 1):
    tc = int(input())

    searchKeyWord = input()
    word = input()

    answer = 0

    for i, val in enumerate(word):                        # 각 단어의 위치에
        if word[i:i+len(searchKeyWord)] == searchKeyWord: # 키워드의 길이에 맞춰 각 단어의 위치에 따라 길이 만큼 슬라이싱한 단어를 찾는 단어와 일치할 때
            answer += 1                                   # 카운팅했다.

    print('#' + str(test_case), answer)



# count()를 사용하면 쉽게 찾을 수 있다.

T = 10

for test_case in range(1, T + 1):
    tc = int(input())

    searchKeyWord = input()
    word = input()

    answer = word.count(searchKeyWord)

    print('#' + str(tc), answer)