N = int(input())
answer = []
    
for i in range(1, N+1):
    if str(i).count('3') > 0 or str(i).count('6') > 0 or str(i).count('9') > 0 :
        count = 0
            
        for j in str(i):
            if int(j) == 3 or int(j) == 6 or int(j) == 9:
                count += 1
            
        answer.append('-' * count)
    else:
        answer.append(i)
    
print(' '.join(map(str, answer)))