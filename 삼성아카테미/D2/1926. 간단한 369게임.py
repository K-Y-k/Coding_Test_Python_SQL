# 3 6 9가 아닐 때는 그대로 정답 리스트에 넣어주고
# 3 6 9일 때는 현재 숫자를 문자로 각 숫자열을 확인해가며 3 6 9의 개수를 카운팅한 후
# '-' x 카운팅 수인 값을 정답 리스트에 넣어준다. 

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