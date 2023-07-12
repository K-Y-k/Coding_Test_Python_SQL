# 내가 푼 방식 : 차이가 중복된 경우 기존 원소 큰 값이 나올 수 없음
# 딕셔너리에 차이를 저장하고 차이 순을 오름차순으로 답을 넣었다.

def solution(numlist, n):
    answer = []
    distance_list = {}
    
    for i in numlist:
        temp = abs(i-n)
        
        distance_list[i] = temp
        
    s = list(sorted(distance_list.items(), key=lambda x:(x[1], x[0])))

    for i in s:
        answer.append(i[0])
    
    
    return answer


# 처음 연산과정에서부터 정렬을 하여 
# 1번째 우선순위인 절대 값 격차가 동일한 경우 2번째 우선순위를 적용하여 큰 값이 나오게 유도하였다. 

def solution(numlist, n):
    answer = []
    answer = sorted(numlist, key=lambda x:(abs(x-n), n-x))


    return answer