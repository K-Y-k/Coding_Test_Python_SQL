# 1. 문자열을 HEAD, NUMBER, TAIL로 구분하여 자른다.
# 2. HEAD를 첫 번째 key, NUMBER를 두 번째 key로 정렬한다.

def solution(files):
    answer = []
    file_split_list = []
    

    for f in files:
        head = ''
        num = ''
        tail = ''
        num_check = False
        
        # 1. 문자열을 HEAD, NUMBER, TAIL로 구분하여 자른다.
        for idx, value in enumerate(f):                
            if value.isdigit():                         # 숫자가 올 경우 이때부터 HEAD는 끝이므로 num_check 킨다.
                num += value
                num_check = True                       
            elif not num_check:                         # 아직 nun_check가 안된 때는 HEAD부분
                head += value
            else:                                       # 숫자가 아닌 문자인데 num_check가 True인 상태이면 TAIL부분
                tail = f[idx:]
                break
                
        file_split_list.append([head, num, tail])

            
    # 2. HEAD를 첫 번째 key, NUMBER를 두 번째 key로 정렬한다.
    file_split_list = sorted(file_split_list, key=lambda x:(x[0].lower(), int(x[1])))   # 1순위는 HEAD의 문자열부터, 2순위는 NUMBER 숫자부분
                                                                                        # int로 숫자로 바꾼 이유는 01과 1이 동일하게 취급한다고 했기 때문
    
    for i in file_split_list:
        answer.append(''.join(i))

    
    return answer



# 시도 해본 방식 : 일부 테케 런타임 에러

def solution(files):
    answer = []
    file_split_list = []

    
    for f in files:
        head = ''
        num = ''
        tail = ''
        
        num_idx = 0
        
        for i in f:
            if i.isdigit():
                num_idx = f.index(i)
                break
            else:
                head += i
                
        for i in range(num_idx, len(f)):
            if not f[i].isdigit():
                tail = f[f.index(f[i]):]
                num = f[num_idx:f.index(f[i])]
                break
                
        
        file_split_list.append([head, num, tail])
            
    
    file_split_list = sorted(file_split_list, key=lambda x:(x[0].lower(), int(x[1])))
    
    for i in file_split_list:
        answer.append(''.join(i))

    
    return answer