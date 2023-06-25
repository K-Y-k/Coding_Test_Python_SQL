# 내가 푼 방식
# 원형순열로 이루어지는 것이므로 같은 elements 배열을 한번 더 이어붙이면 연속된 부분으로 가져올 수 있다.
# 중복이 발생할 수 있으므로 set으로 중복처리를 해주어야 한다.


def solution(elements):
    answer = 0
    new_elements = []                                        # 연속으로 이어 붙인 것들의 합을 넣을 리스트 선언
    elements = elements*2                                    # 원형순열로 이루어지는 것이므로 같은 elements 배열을 한번 더 이어붙이면 연속된 부분으로 가져올 수 있다.
    
    for length in range(1, len(elements)//2+1):
        for i in range(0, len(elements)//2+1):
            new_elements.append(sum(elements[i:i+length]))   # 길이만큼 연속 이어진 것의 합을 새로 넣어준다.
            
    answer = len(set(new_elements))                          # 중복이 발생할 수 있으므로 set으로 중복처리를 해주어야 한다.
    
    return answer
