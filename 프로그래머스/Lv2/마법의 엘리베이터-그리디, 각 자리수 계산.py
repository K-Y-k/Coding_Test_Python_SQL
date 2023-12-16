# 문제의 원리
# 각 자리수에서 5보다 크면 10-현재 자리수의 값으로 답에 적용하고 다음 자리수의 값도 올려주고
#              5보다 작으면 현재 자리수의 값으로 답에 적용하고
#              5이면 다음 자리수를 확인하여 5보다 크면 다음 자리수의 값도 올려주고 답에 적용


# 내가 푼 방식
# 각 자리수를 리스트로 담고
# 제일 뒤의 원소를 꺼내와 비교하며 했지만
# 이렇게하면 다음 자리수가 9이면 다다음 자리수의 갱신이 불가능하다

def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))
    
    
    while len(storey) != 0:
        x = storey.pop()
        
        if x > 5:
            answer += 10-x
            storey[-1] += 1
        elif x < 5:
            answer += x
        else:
            if storey[-1] >= 5:
                storey[-1] += 1
                answer += x
            else:
                answer += x
    

    return answer



# 그렇기에 %10 와 //10를 활용해 전체 숫자를 가져와서 적용해가야한다.

def solution(storey):
    answer = 0

    while storey != 0:
        x = storey % 10
        
        if x > 5:
            answer += 10-x
            storey += 10
        elif x < 5:
            answer += x
        else:
            if (storey // 10) % 10 >= 5:
                storey += 10
                answer += x
            else:
                answer += x
            
        storey //= 10


    return answer