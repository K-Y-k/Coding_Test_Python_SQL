# 내가 푼 방식 -> 효율성 테스트 실패 
# 하나의 기준 값을 리스트에 넣고 그 기준 값과 루프를 돌면서의 값의 합이 limit보다 작거나 같으면 
# 기존에 저장된 리스트가 2개있으면 서로 비교해서 limit에 가깝게 큰 값이 들어가게 하여 최대한 몸무게를 싫어 이동횟수를 최소화 시켰다.


def solution(people, limit):
    answer = 0
        
    while len(people) > 0:
        temp = []                                           # 배에 탈 사람의 리스트
        
        for i in people:                   
            if len(temp) == 0:                              # 아직 아무도 안 탔을 경우 현재 값을 기준 값으로 넣는다.
                temp.append(i)
            else:                                           # 한명이상이 타져있는 상황에서
                if i + temp[0] <= limit and len(temp) == 2: # 2명이 이미 타진 상황인데 현재 값 + 기준 값이 limit의 조건일 때
                    if i + temp[0] > sum(temp):             # 현재 값 + 기준 값과 기존에 temp 값을 합한 값과 비교하여 현재 값 + 기준 값이 크다면
                        temp.pop()                          # 기존 temp에서 끝 값을 지워주고
                        temp.append(i)                      # 현재 값으로 넣어준다.

                elif i + temp[0] <= limit:                  # limit의 조건이 되는데 아직 temp에 한명만 있으면 그냥 넣어주기
                    temp.append(i)
                    
        for i in temp:                                      # 배에 타고 간 사람은 제거해주기
            people.remove(i)
        
        answer += 1                                         # 배에 한번 이동한 카운팅처리
    
    return answer



# 효율성 테스트 통과 방식 : 투포인터 사용
# 포인터 위치를 2개를 잡고 조건을 따져주면서 정답을 찾아주는것

# 구명보트에 2명을 태워야하는데 최소한으로 구명보트를 이용해야하기 때문에 
# 가장 몸무게가 많이 나가는 사람과 적게 나가는 사람을 계속해서 매칭시켜서 최대한 한번에 태워보내주면 최소값을 찾아줄 수 있다.

# 그러기 위해서는 먼저 people의 list를 정렬을 해주어야한다.
# 이후 left와 right포인터 위치의 값의 합이 limit을 넘지 않으면 한번에 태워보내는 것이다. 
# 만약 limit를 넘게 된다면 작은사람은 다른사람과 태워서 보내면 limit을 넘지 않을 수도 있기 때문에 무거운사람을 하나 태워서 보내는것이다.

def solution(people, limit):
    answer = 0
    people.sort()                                    # 정렬 처리

    left = 0                                         # 시작 값
    right = len(people)-1                            # 끝의 값
    
    while left <= right:                             # 시작 값과 끝의 값이 엇갈리지 않을 때까지 반복
        if people[left] + people[right] <= limit:    # 조건에 맞을 경우
            left += 1                                # 가벼운 사람과 무거운 사람을 같이 태워 보낸 것으로 서로 한칸씩 땡긴다.
            right -= 1
        else:                                        # 조건에 안 맞으면 오른쪽의 끝의 값만 땡긴다. 무거운사람을 하나 태워서 보낸 것이다.
            right -= 1                               
        
        answer += 1                                  # 배에 태워 보낸 것을 카운팅
    
    return answer