# 내가 푼 방식 : 일부 케이스 실패
# 각 방식 3가지를 차례로 최대한 적용하고 카운팅한 값을 반환했지만
# 아무래도 차례로 적용했으므로 일부 케이스만 성공한 것이었다.
# 문제에서 원하는 것은 각 경우만 최대한 연산하는 것이 아닌 각 3가지 연산을 섞어가며 적용해가는 것이었다.

def solution(x, y, n):
    answer = 0
    answer_li = []
    
    
    # 곱하기 3 경우
    tmp_y = y
    count = 0
    while tmp_y >= x:
        if tmp_y == x:
            answer_li.append(count)
            break
        
        if int(tmp_y) != tmp_y :
            break
        
        if tmp_y % 3 == 0:
            tmp_y /= 3
        else:
            tmp_y -= n
        
        count += 1
    
    # 곱하기 2 경우
    tmp_y = y
    count = 0
    while tmp_y >= x:
        if tmp_y == x:
            answer_li.append(count)
            break
        
        if int(tmp_y) != tmp_y :
            break
        
        if tmp_y % 2 == 0:
            tmp_y /= 2
        else:
            tmp_y -= n
        
        count += 1
    
    # + n 경우
    tmp_y = y
    count = 0
    while tmp_y >= x:
        if tmp_y == x:
            answer_li.append(count)
            break
            
        tmp_y -= n
        
        count += 1
    

    if answer_li:
        answer = min(answer_li)
    else:
        answer = -1
    
    
    
    return answer



# set() + bfs 방식
# 같은 수가 들어갈 수 있는데 이러면 같은 값이 나오는 연산을 중복하게 되어 시간이 비효율적이므로 중복을 방지하기 위해 set()을 사용한다. 
# n을 더하는 방법 / 2를 곱하는 방법 / 3을 곱하는 방법을 적용한 각 연산들을 dp에 넣으면서 카운팅하고
# 정답의 값이 들어 있으면 카운팅한 값을 반환하고
# 각 3가지 방법을 적용해가다가 모든 방법으로 적용했는데 정답의 값보다 크게 되면 답이 나올 수 없으므로 
# dp 안에 값이 비게되어 while문을 탈출하고 -1을 반환하도록 한다. 

def solution(x, y, n):
    answer = 0
    dp = set()                 # 같은 수가 들어갈 수 있는데 이러면 같은 연산을 하므로 시간이 비효율적이므로 중복을 방지하기 위해 set()을 사용한다. 
    dp.add(x)
    
    while dp:                  # 각 3가지 방법을 적용해가다가 모든 방법으로 적용했는데 정답의 값보다 크게 되면 답이 나올 수 없으므로 
                               # dp 안에 값이 비게되어 while문을 탈출하고 -1을 반환하도록 한다. 

        if y in dp:            # 정답의 값이 들어 있으면 카운팅한 값을 반환하고
            return answer
        
        dp_y = set()
        
        for i in dp:           # n을 더하는 방법 / 2를 곱하는 방법 / 3을 곱하는 방법을 적용한 각 연산들을
            if i+n <= y:
                dp_y.add(i+n)
            if i*2 <= y:
                dp_y.add(i*2)
            if i*3 <= y:
                dp_y.add(i*3)
        
        dp = dp_y             # dp에 넣으면서 
        answer += 1           # 카운팅하고
            
    return -1