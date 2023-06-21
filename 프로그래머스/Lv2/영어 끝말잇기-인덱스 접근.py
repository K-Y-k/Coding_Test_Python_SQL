# 처음에는 자신이 몇번째 번호의 사람인지와 몇번째 단어를 외쳤는지의 인덱스를 정하고
# 단어가 중복된 경우이거나 이전 단어의 끝자리와 현재 단어의 앞자리의 글자가 다르면 


def solution(n, words):
    answer = []
    set_word = []                                                         # 중복 단어를 검사하기 위한 리스트
    count = [0] * (n+1)                                                   # 몇번째로 단어를 외친 차례인지를 선언 
    
    
    for i, value in enumerate(words):
        count_idx = (i+1) % n                                             # 현재 사람의 번호 확인
        if count_idx == 0:
            count_idx = n
            
        count[count_idx] += 1                                             # 자신이 몇번째 차례인지와 몇번째 단어를 외쳤는지 카운팅
        
        
        if value in set_word or words[i-1][-1] != value[0] and i > 0:     # 단어가 중복된 경우이거나 이전 단어의 끝자리와 현재 단어의 앞자리의 글자가 다르면 
            answer.append(count_idx)                                      # 탈락한 사람의 번호와
            answer.append(count[count_idx])                               # 자신이 몇번째 차례인지와 몇번째 단어를 외쳤는지를 답에 넣고 반복 종료
            break
        else:
            set_word.append(value)
            
            
        if i == len(words)-1 and value in set_word:                        # 마지막 단어까지 모두 진행해도 위 필터에 걸치지 않았다면 
            return [0, 0]
            

    return answer