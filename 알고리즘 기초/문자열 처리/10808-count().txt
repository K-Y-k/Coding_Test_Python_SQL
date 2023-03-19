word = str(input())

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

result = ''

for i in alpha_list:
    result += str(word.count(i)) + ' '   # count함수는 int형으로 반환하므로 여기서는 result가 string이므로 형변환 주의
                                               
print(result)