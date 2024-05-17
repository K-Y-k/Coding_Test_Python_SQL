# 각 라인별로 .과 #의 일정한 패턴을 파악한 후 적용해주고
# 가운데 세번째 라인은 for문으로 문자 수 만큼의 패턴을 적용해준다. 

word = input()
answer = []

first_line = '..#.'
second_line = '.#.#'
third_line = '#.'
third_line_total = ''

print(first_line * len(word) + '.')
print(second_line * len(word) + '.')

for i in range(len(word)):
    third_line_total += third_line + word[i] + '.'

    if i == len(word)-1:
        third_line_total += '#'
        
print(third_line_total)

print(second_line * len(word) + '.')
print(first_line * len(word) + '.')
