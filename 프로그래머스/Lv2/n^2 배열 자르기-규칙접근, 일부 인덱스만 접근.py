# 내가 푼 방식 : 직접 모든 값을 넣은 1차원 배열 생성하여 슬라이스 => 일부 테스트 케이스 시간 초과
# 문제에서 10^7까지라고 했기에 n번 모두 반복 조회하면 안된다.

def solution(n, left, right):
    answer = []
    
    for i in range(1, n+1):
        temp = []
            
        for j in range(i, n+1):
            if j == i:
                for _ in range(j):
                    temp.append(i)
            else:
                temp.append(j)
                
            if len(temp) == n:
                for k in temp:
                    answer.append(k)
                break
    
    return answer[left:right+1]



# 규칙을 파악하고 문제에서 원하는 인덱스만 가져오기

# 예시로 n이 3인 것만 일 때
# 실제 값   :   1      2      3      2      2      3      3      3      3
# 인덱스 값 :   0      1      2      3      4      5      6      7      8
# x,y 위치  : (0,0)  (0,1)  (0,2)  (1,0)  (1,1)  (1,2)  (2,0)  (2,1)  (2,2) 

# 만약 left가 2이면 x좌표 값은 '현재 인덱스 // n'이고 y좌표 값은 '현재 인덱스 % n'이다.
# 그리고 현재 x, y좌표의 가장 큰 값에 +1이 실제 값이 된다. 

def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        x = i // n                               # x좌표 값은 '현재 인덱스 // n'
        y = i % n                                # y좌표 값은 '현재 인덱스 % n'
        
        answer.append(max(x, y)+1)               # 현재 x, y좌표의 가장 큰 값에 +1이 실제 값이 된다.
    
    return answer