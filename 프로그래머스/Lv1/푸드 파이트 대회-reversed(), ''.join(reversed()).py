# 내가 푼 방식은 
# 1. 짝수가 되는 숫자만 가능하므로 짝수로 맞춰진 개수로 새로 담았고
# 2. 새로 담은 짝수 개수만큼의 절반만 해당 값을 앞에 두고
# 3. 0인 물병은 항상 1개이므로 따로 넣었고
# 4. 나머지 위에서 남은 절반만큼 역순으로 넣었다.

def solution(food):
    answer = ''
    new_food = []
    
    for i, value in enumerate(food):                   # 1. 짝수가 되는 숫자만 가능하므로 짝수로 맞춰진 개수로 새로 담았고
        if i != 0 and value % 2 == 0:
            new_food.append(value)
        elif i != 0 and value % 2 != 0:
            new_food.append(value-1)
        else:
            new_food.append(value)
            
        
    for i, value in enumerate(new_food):              # 2. 새로 담은 짝수 개수만큼의 절반만 해당 값을 앞에 두고
        if i != 0:
            for j in range(value//2):
                answer += str(i)
                
    answer += '0'                                     # 3. 0인 물병은 항상 1개이므로 따로 넣었고
    
    for i, value in enumerate(reversed(new_food)):    # 4. 나머지 위에서 남은 절반만큼 역순으로 넣었다.
        if i != len(new_food)-1:
            for j in range(value//2):
                answer += str(len(new_food)-i-1)
    
    
    return answer



# 배운점 : 현재 문자열을 뒤집고 싶을 경우 = ''.join(reversed(문자열))
# 위 역순으로 넣는 것이 복잡하여 ''.join(reversed(answer))로 좀 더 깔끔하게 개선하였다.

def solution(food):
    answer = ''
    new_food = []
    
    for i, value in enumerate(food):
        if i != 0 and value % 2 == 0:
            new_food.append(value)
        elif i != 0 and value % 2 != 0:
            new_food.append(value-1)
        else:
            new_food.append(value)
            
        
    for i, value in enumerate(new_food):
        if i != 0:
            for j in range(value//2):
                answer += str(i)
                
    reversed_answer = ''.join(reversed(answer))      # 위 역순 방식이 복잡하여 문자열을 역으로 뒤집어서 저장하고 
    answer += '0'                                    # 0을 넣은 후
    answer += reversed_answer                        # 위에 저장했던 뒤집은 문자를 넣어주었다.
    
    
    return answer