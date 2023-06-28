# 내가 처음에 접근한 방식 : 피로도 최소로 정렬한 후 구하려고 함
# 하지만 최소 피로도의 상황에 따라 달라져 이렇게 접근하면 안되었다..

def solution(k, dungeons):
    answer = 0
    s = sorted(dungeons, key=lambda x:x[1])
    
    for i in range(0, len(s)):
        print(k)
        if s[i][0] <= k:
            k -= s[i][1]
            answer += 1
    
    
    return answer



# 순열을 이용해 모든 경우의 수를 담아서 각 케이스의 최대 값으로 담기

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    p = permutations(dungeons, len(dungeons))         # 순열을 이용해 모든 경우의 수를 담아서
    
    for i in p:                                       # 각 케이스를 모두 조회하여
        temp_k = k                                    # 각 케이스 계산을 위한 k의 값 변수
        temp_count = 0                                # 각 케이스에서 던전 피로도 소모를 성공한 횟수 
        
        for j in i:
            if j[0] <= temp_k:                        # 최소 피로도에 해당하면 k를 빼고 소모 성공 횟수 갱신
                temp_k -= j[1]
                temp_count += 1
            else:
                break

        answer = max(temp_count,answer)               # 위 연산을 완료한 해당 케이스의 성공 횟수 최대 값으로 갱신
            

    return answer