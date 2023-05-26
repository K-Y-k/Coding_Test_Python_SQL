# 정렬후 startswith 방식: 다음 번호 문자가 접두어를 가지는지 startswith()를 이용해 확인할 수 있다. 

def solution(phone_book):
    answer = True
    
    phone_book.sort()                                  # 차례로 접두어를 검사하기 위해 문자 길이 순으로 정렬
    
    for i in range(len(phone_book)-1):                 # 아래 다음 원소를 비교하는 과정이 있어 인덱스 범위를 초과하지 않게 -1 해야함 
        if phone_book[i+1].startswith(phone_book[i]):  # 다음 원소 번호가 현재 번호가 접두어인지 확인해서 사실이면
            return False                               # False 반환
    
    return answer




# 딕셔너리를 사용한 방식: 각 번호를 딕셔너리에 담고
#                        전화번호부를 각 조회할 때 각 번호 하나씩 접두사에 추가하면서 
#                        현재 접두사가 딕셔너리에 담긴 것이 있지만 전화번호부의 전체 형태가 동일하지 않는 것이면 접두사가 겹친 것이므로 False 

def solution(phone_book):
    answer = True
    temp = {}
    
    for i in phone_book:
        temp[i] = 1
        
    for phone_number in phone_book:
        jubdoo = ''
        
        for num in phone_number:
            jubdoo += num                                 # 번호를 하나씩 접두사에 추가하면서
            
            if jubdoo in temp and jubdoo != phone_number: # 현재 접두사가 딕셔너리에 담긴 것이 있지만 전화번호부의 전체 형태가 동일하지 않는 것이면
                return False                              # 접두사가 겹친 것이므로 False 
        
    
    return answer
