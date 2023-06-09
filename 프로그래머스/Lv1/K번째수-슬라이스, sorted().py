# 내가 풀어본 방식(비효율)
def solution(array, commands):
    answer = []
    
    for command in commands:
        new_array = []                         # 새로 슬라이스한 것을 넣기 위한 배열 선언
        
        if command[0] != command[1]:
            for a in range(command[0]-1, command[1]):
                new_array.append(array[a])
            new_array.sort()
        else:
            new_array.append(array[command[0]-1])

        answer.append(new_array[command[2]-1])
    
    return answer



# 효율적으로 개선한 방식
# 1. 필요한 원소 값을 따로 변수에 담기
# 2. if문을 굳이 할 필요 없이 바로 넣기
def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command                   # 1. command[0], command[1], command[2]를 이렇게 한번에 변수에 담을 수 있다.
        new_array = [] 
        
        new_array = sorted(array[i-1:j])    #    변수로 담았기에 표현이 더 직관적이게 됐다.

        answer.append(new_array[k-1])       # 2. if문으로 굳이 command를 비교하지 않고 바로 command[2]인 k를 넣어 정답에 넣는다.

    return answer