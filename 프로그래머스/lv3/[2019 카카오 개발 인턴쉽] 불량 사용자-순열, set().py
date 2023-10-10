# 순열을 이용해서 모든 경우의 수를 가져오고
# 각 경우의 목록과 제한 목록의 아이디를 서로 비교하여 판별한 후
# 문제에서 아이디의 순서는 상관없다고 했으므로 set()으로 중복이 있는지 검사한 후 없으면 정답 리스트에 넣어주어
# 최종 정답 리스트의 길이가 나올 수 있는 경우의 수이다.

from itertools import permutations

def check(id_list, banned_list):                   # 경우의 목록과 제한 목록의 아이디와 동일한지 검사하는 함수
    for i in range(len(id_list)):
        if len(id_list[i]) != len(banned_list[i]): # 경우의 목록의 아이디와 제한 목록의 아이디의 길이가 서로 맞지 않는다면 False 반환
            return False
        
        for j in range(len(id_list[i])):           
            if banned_list[i][j] == "*":           # "*"는 그대로 진행
                continue
                
            if id_list[i][j] != banned_list[i][j]: # 서로의 스펠이 맞지 않으면 False 반환
                return False
    
    return True                                    # 위에서 모든 반복을 거쳤으면 모두 맞는 것이므로 True 반환
        

def solution(user_id, banned_id):
    answer = []
    
    p = permutations(user_id, len(banned_id))      # 각 경우의 리스트를 저장
    
    for id_list in p:                              # permutations에서 각 경우의 리스트를 하나씩 가져와서
        if check(id_list, banned_id):              # 제한 목록의 아이디와 검사해서 True로 통과되면
            if set(id_list) not in answer:         # 정답 리스트에 해당 목록이 겹치지 않으면 정답 리스트에 넣기
                answer.append(set(id_list))           
    
    return len(answer)                             # 중복값이 제거된 정답 리스트의 길이 출력