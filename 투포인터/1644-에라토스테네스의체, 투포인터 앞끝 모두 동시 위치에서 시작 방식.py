# 에라토스테네스의 체로 2부터 N까지의 값중 소수를 판별해준 후 소수인 것은 소수 리스트에 따로 넣어주고 
# 주의점은 부분합을 갱신해나가므로 합의 초깃값을 넣어줘야 하고 끝의 값도 적용해주려면 끝에 0의 값을 넣어야 했다.
# 소수 리스트의 앞, 끝 포인터를 앞부터 동시에 시작하여
# 1) 현재 앞~끝 포인터의 합이 N인 경우 정답이므로 카운팅해준후 
#    현재 포인터에서의 같은 경우는 더이상 없으므로 
#    앞의 포인터는 한칸 전진하고 전진했으므로 이전 값을 합에서 빼주고 
#    뒤의 포인터도 한칸 전진하고 전진했으므로 전진한 값을 합에서 더해주어 최신화해준다. 
# 2) 현재 앞~끝 포인터의 합이 N보다 크면 합이 더 작아야하므로 앞의 포인터를 한칸 전진하고 전진했으므로 이전 값을 합에서 빼준다.
# 3) 현재 앞~끝 포인터의 합이 N보다 작으면 합이 더 커야하므로 끝의 포인터를 한칸 전진하고 전진했으므로 전진한 값을 합에서 더해준다.

N = int(input())
prime_li = []

# 에라토스테네스의 체
num_arr = [True] * (N+1)
num_arr[0] = False
num_arr[1] = False

for i in range(2, N+1):                           # 에라토스테네스의 체로 2부터 N까지의 값중 소수를 판별해준 후
    if num_arr[i]:
        j = i * i

        while j <= N:
            num_arr[j] = False
            j += i

for i in range(2, N+1):                           # 소수인 것은 소수 리스트에 따로 넣어주고 
    if num_arr[i]:
        prime_li.append(i)

prime_li.append(0)                                # 주의점은 부분합을 갱신해나가므로 끝의 값도 적용해주려면 끝에 0의 값을 넣어야 했다.

total = prime_li[0]                               # 주의점은 부분합을 갱신해나가므로 합의 초깃값을 넣어줘야 한다. 
answer = 0

left = 0                                          # 소수 리스트의 앞, 끝 포인터를 앞부터 동시에 시작하여
right = 0

while right < len(prime_li)-1:                    # 여기서 전체길이 -1보다 작아야하는 이유는 끝에 0의 값을 넣었으로
    if total == N:                                # 1) 현재 앞~끝 포인터의 합이 N인 경우
        answer += 1                               #    정답이므로 카운팅해준후 
                                                  #    현재 포인터에서의 같은 경우는 더이상 없으므로
        total -= prime_li[left]                   #    앞의 포인터는 한칸 전진하고 전진했으므로 이전 값을 합에서 빼주고 
        left += 1

        right += 1                                #    뒤의 포인터도 한칸 전진하고 전진했으므로 전진한 값을 합에서 더해준다. 
        total += prime_li[right]
    elif total > N:                               # 2) 현재 앞~끝 포인터의 합이 N보다 크면 합이 더 작아야하므로
        total -= prime_li[left]                   #    앞의 포인터를 한칸 전진하고 전진했으므로 이전 값을 합에서 빼준다.
        left += 1
    elif total < N:                               # 3) 현재 앞~끝 포인터의 합이 N보다 작으면 합이 더 커야하므로
        right += 1                                #    끝의 포인터를 한칸 전진하고 전진했으므로 전진한 값을 합에서 더해준다.
        total += prime_li[right]

print(answer)




# 다른 방식

import math

N = int(input())
prime_li = []

# 에라토스테네스의 체
num_arr = [True]*(N+1)
num_arr[0] = False
num_arr[1] = False

for i in range(2, int(math.sqrt(N))+1):
    if num_arr[i]:
        for j in range(i*2, N+1, i):
            num_arr[j] = False

for i in range(2, N+1):
    if num_arr[i]:
        prime_li.append(i)


left = 0
right = 0
answer = 0

while right <= len(prime_li)-1:
    temp = sum(prime_li[left:right+1])

    if temp == N:
        answer += 1
        right += 1
    elif temp > N:
        left += 1
    elif temp < N:
        right += 1

print(answer)