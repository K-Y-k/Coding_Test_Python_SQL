# 처음에는 다리에 제한된 트럭 개수만큼 공간을 만들고 그 공간을 한칸씩 옆으로 이동해서 도착시켜야하는 것을 알아차리지 못했다..

# 다리에 제한된 트럭 개수만큼의 공간을 만들고
# 다리의 공간이 0이 될 때까지 반복하여
# 시간 카운팅을 먼저 처리한 후 
# 다리의 제일 앞의 값을 빼고 
# 남은 트럭이 존재하면 현재 다리의 무게와 트럭의 제일 앞의 무게의 합이 제한된 최대무게에 걸치면 남은 트럭에서 빼와서 다리에 넣고
# 최대무게보다 초과하면 위에서 다리 제일 앞의 값을 뺐으므로 다시 그 공간을 채워야해서 0을 넣어야한다.

from collections import deque

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([0] * w)                              # 다리에 제한된 트럭 개수만큼의 공간을 만들고
count = 0

while bridge:                                        # 다리의 공간이 0이 될 때까지 반복하여
    count += 1                                       # 시간 카운팅을 먼저 처리한 후 
    bridge.popleft()                                 # 다리의 제일 앞의 값을 빼고 

    if trucks:                                       # 남은 트럭이 존재하면
        if sum(bridge) + trucks[0] <= L:             # 현재 다리의 무게와 트럭의 제일 앞의 무게의 합이 제한된 최대무게에 걸치면 남은 트럭에서 빼와서 다리에 넣고
            bridge.append(trucks.popleft())
        else:                                        # 최대무게보다 초과하면 위에서 다리 제일 앞의 값을 뺐으므로 다시 그 공간을 채워야해서 0을 넣어야한다.
            bridge.append(0)


print(count)