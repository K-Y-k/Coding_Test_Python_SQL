from collections import deque

N, K = list(map(int, input().split()))

N_list = deque()
result = []

for i in range(1, N+1):
    N_list.append(i)


for _ in range(N):
    N_list.rotate(-(K-1))             
    result.append(str(N_list.popleft()))
    
print('<' + ', '.join(result) +'>')