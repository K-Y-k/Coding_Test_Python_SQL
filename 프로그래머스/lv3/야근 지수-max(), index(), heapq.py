# 내가 푼 방식 : 효율성 테스트 실패
# 제곱으로 일의 지수가 계산되는 것을 보고 각 일 지수 중 가장 큰 값을 하나씩 빼야겠다는 생각을 했고
# max()로 일의 지수가 가장 큰 것을 가져온 후 그 위치의 인덱스 값에서 -1을 하여 일의 지수를 낮추었다.
# 하지만 index(max(works)) 이렇게하면 반복할 때마다 최대 값에 인덱스를 찾아야 하는 작업 때문에 효율성에서 실패하게 된다. 

def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return 0
    

    for _ in range(n):
        works[works.index(max(works))] -= 1  # max()로 일의 지수가 가장 큰 것을 가져온 후 그 위치의 인덱스 값에서 -1을 하여 일의 지수를 낮추었다.
        
    
    for i in works:
        answer += i ** 2
    
    
    return answer



# 힙을 활용한 방식
# 힙을 사용해서 원소 값이 자동으로 정렬되게 적용하여 반복할 때마다 최대 값을 일일히 찾지 않게 해준다.

import heapq

def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return 0
    
    works = [-i for i in works]                 # -로 한 적용한 이유는 최대 값순으로 정렬하고 싶기 때문이다. 
    
    heapq.heapify(works)                        # 해당 배열을 힙으로 적용하고
    
    for _ in range(n):
        max_value = heapq.heappop(works)        # 제일 앞의 최대 값을 꺼내오고 
        heapq.heappush(works, max_value + 1)    # -최대값이므로 -1이 아닌 +1로 차감해준 값으로 다시 넣어 최신화해준다.
        
    
    for i in works:
        answer += i ** 2                        # 어차피 제곱으로 넣기에 -로 적용한 것을 그대로 두어도 문제 없는 것
    
    
    return answer