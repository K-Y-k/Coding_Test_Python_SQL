# 문제에서 분해합이 현재 값 + 현재값의 각 자리수 합이므로
# 1부터 주어진 값까지 조회하여 분해합을 적용하여 값이 맞으면 정답

N = int(input())
answer = 0

for i in range(1, N):
    x = str(i)
    part_sum = 0
    
    for j in x:
        part_sum += int(j)
    
    part_sum += int(x)
    
    if part_sum == N:
        answer = int(i)
        break
        
print(answer)