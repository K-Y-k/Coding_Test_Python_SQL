# 내가 푼 방식 : for 루프 모든 값을 조회하기에 시간초과로 일부 테스트 실패

def solution(number, limit, power):
    answer = 0
    count_list = []
    
    for i in range(1, number+1):            # 1~number까지 모두 조회하여
        count = get_count(i)                  # 약수의 개수 파악한 후 
        count_list.append(count)            # 약수 개수 리스트에 넣음
    
    for i in count_list:                    # 약수 개수 리스트를 조회하여
        if i > limit:                       # 제한 수 보다 크면
            answer += power                 # power 값만큼 상승
        else:                               # 제한 수 보다 작으면
            answer += i                     # 현재 값 그대로 상승
    
    return answer

def get_count(number):                        # 약수 개수 파악하는 함수 선언
    count = 0                               # 개수 0으로 초기화
    
    if number == 1:                         # 1이면 약수의 개수는 무조건 1이므로 1로 반환
        return 1
    else:                                   # 그외의 숫자면 
        for i in range(1, number+1):        # 1부터 받아온 숫자까지 조회하여
            if number % i == 0:             # 약수이면
                count += 1                  # 1 상승
            
    return count



# 약수의 개수 효율성 방식 : 제곱근까지만 접근하기
# for문을 돌릴 때, int(제곱근)까지만 반복하는 것이다.
# ex) 18의 제곱근은 4.xxx정도가 나온다.
#     for문을 돌리면 1, 2, 3, 4가 각각 18의 약수인지를 볼 것이다.
#     [1, 2, 3]이 각각 카운트되고, 18을 각각의 약수들로 나눈 [18, 9, 6]도 카운트 된다.

def solution(number, limit, power):
    answer = 0
    count_list = []
    
    for i in range(1, number+1):
        count = get_count(i)
        count_list.append(count)
        
    for i in count_list:
        if i > limit:
            answer += power                
        else:                             
            answer += i       

    return answer
    
def get_count(number):
    count = 0
    
    if number == 1:
        return 1
    else:
        for i in range(1, int(number**(0.5))+1):    # 제곱근만큼만 조회하여
            if number % i == 0:
                if i == number // i:                #  제곱근일 경우
                    count += 1                      #  1개만 카운트하기

                else:                               #  제곱근이 아닐 경우
                    count += 2                      #  2개 카운트 (i, n//i)

    return count
            