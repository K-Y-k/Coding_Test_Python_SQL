word = input()

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in alpha_list:
    if i in word:
        result = word.index(i)
    else:
        result = -1
    print(result, end= ' ')             # 출력할 때 끝에 공백을 주게한다.