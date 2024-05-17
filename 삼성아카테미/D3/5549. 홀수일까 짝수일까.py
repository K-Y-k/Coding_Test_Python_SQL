# 나머지에 따른 홀수 짝수 구분하기

num = int(input())
answer = ''

if num % 2 == 0:
    answer = 'Even'
else:
    answer = 'Odd'

print(answer)