# nums의 숫자가 포켓몬 종류로 종류별로 딕셔너리에 담아 개수를 카운팅한다.
# nums의 총 개수의 절반이 포켓몬을 가져갈 수 있는 최대 개수이므로
# 종류별로 담은 딕셔너리의 총 길이에 따른 포켓몬 종류 개수를 출력할 수 있다. 


def solution(nums):
    answer = 0
    pocket_dic = {}
    
    for i in nums:                             # nums의 숫자가 포켓몬 종류로 종류별로 딕셔너리에 담아 개수를 카운팅한다.
        if i not in pocket_dic:
            pocket_dic[i] = 1
        else:
            pocket_dic[i] += 1
            
    count = len(nums) // 2                     # nums의 총 개수의 절반이 포켓몬을 가져갈 수 있는 최대 개수이므로
    result_count = len(pocket_dic) - count     # 딕셔너리의 종류 길이에서 가져갈 수 있는 최대 개수를 뺀 것을 기준으로 삼아서
    
    if result_count >= 0:                      # 해당 기준에 종류별로 담은 딕셔너리의 총 길이에 따른 포켓몬 종류 개수를 답에 넣는다. 
        answer = count
    else:
        answer = len(pocket_dic)
        
    
    return answer