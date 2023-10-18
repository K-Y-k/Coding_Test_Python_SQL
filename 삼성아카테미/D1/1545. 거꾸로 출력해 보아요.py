N = int(input())

li = []

for i in range(0, N+1):
    li.append(i)
    
li.reverse()

answer = ''

for i in li:
    answer += (str(i) + ' ')
    
print(answer)