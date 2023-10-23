# 내가 시도한 방식 = 일부 테케만 맞음
# 10개씩 문자가 차면 정답 리스트에 넣어서 출력할 때 리스트의 원소대로 출력시키면 10개씩인 원소들이 출력될 것이라 생각하였다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    word_li = ''
    answer = []
    
    for i in range(N):
        word, count = map(str, input().split())
        word_li += word * int(count)
    
    
    new_zip = ''
    
    for i, value in enumerate(word_li):
        if (i+1) % 10 == 0:
            answer.append(new_zip)
            new_zip = ''
        else:
            new_zip += value
    else:
        answer.append(new_zip)
    
    print('#' + str(test_case))
    
    for i in answer:
        print(i)
    
    print()



# 정답
# 처음부터 end=''으로 이어 붙이다가 10개째의 단어가 오면 개행되게 구현

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    word_li = ''

    for i in range(N):
        word, count = map(str, input().split())
        word_li += word * int(count)
    
    
    print('#' + str(test_case))
    
    for i, value in enumerate(word_li):
        if (i+1) % 10 == 0:
            print(value)
        else:
            print(value, end='')
            
    print()