N = int(input())

answer = ''

for i in range(0, N+1):
    answer += (str(2**i) + ' ')
    
print(answer)