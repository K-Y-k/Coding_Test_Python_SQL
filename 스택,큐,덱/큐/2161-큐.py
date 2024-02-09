# 1~입력한 숫자까지 큐에 넣고
# 문제에서 주어진 패턴대로 
# 제일 앞의 값을 뺀후 또 제일 앞의 값을 빼서 뒤로 넣어주는 작업을 큐의 길이가 1개가 남을 때 까지 반복한다.

from collections import deque

N = int(input())

q = deque()

for i in range(1, N+1):
    q.append(i)


while len(q) > 1:           # 큐의 길이가 1개가 남을 때 까지 반복한다.
    print(q[0])
    
    q.popleft()             # 제일 앞의 값을 뺀후
    q.append(q.popleft())   # 제일 앞의 값을 빼서 뒤로 넣어준다.


print(q[0])
