# 주어진 알파벳 문자와 입력 받은 문자의 각 위치에서의 알파벳이 동일하면 카운팅하고
# 다르면 그때 멈추고 카운팅한 값을 출력

T = int(input())
alpha_str = 'abcdefghijklmnopqrstuvwxyz'

for test_case in range(1, T + 1):
    word = input()
    answer = 0

    for i in range(len(word)):
        if word[i] == alpha_str[i]:
            answer += 1
        else:
            break

    print('#' + str(test_case), answer)