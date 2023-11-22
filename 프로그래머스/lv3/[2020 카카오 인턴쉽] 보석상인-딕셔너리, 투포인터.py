# 내가 시도한 방식 = 일부 테케 실패 및 효율성 실패
# 이중 루프로 각 원소 위치에서부터 끝까지 하나씩 조회해가며 현재 슬라이싱의 보석들을 set으로 중복을 지운 후의 종류 수를 비교해
# 같으면 정답에 넣고
# 정답에 들어간 범위에서 정렬로 간격 차이가 작은 순부터 오름차순으로 정렬하여
# 맨 첫 원소 값이 답으로 했지만, 
# 모든 원소를 탐색하므로 일부 테케의 시간 초과 발생 및 효율성 제로 

def solution(gems):
    answer = []

    for i in range(len(gems)):
        for j in range(len(gems)+1):
            if len(set(gems[i:j])) == len(set(gems)):
                answer.append([i+1, j])
                
    answer.sort(key=lambda x: x[1]-x[0])
    answer = answer[0]
    
    return answer
        


# 딕녀셔너리의 투포인터 활용 방식

def solution(gems):
    answer = [0, len(gems)-1]     # 첫번째 값 ~ 끝까지의 범위로 초기화한 정답 변수 선언

    kind_size = len(set(gems))    # 보석 종류 개수
    dic = {gems[0]:1}             # 종류 체크할 딕셔너리 선언 및 첫번째 값 초기화

    start, end = 0, 0             # 투포인터

    while start < len(gems) and end < len(gems):
        if len(dic) < kind_size:                        # 종류 개수가 부족하면 딕셔너리 개수 증가
            end += 1                                    # end point 증가
            if end == len(gems):                        # 끝까지 도달했을 경우는 종료
                break

            if gems[end] in dic.keys():                 # 딕셔너리의 해당 값의 개수 증가
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1
            # 위 코드를 간추린 것         -> dic[gems[end]] = dic.get(gems[end], 0) + 1 
            
        else:                                           # 종류 개수가 같으면
            if end-start < answer[1]-answer[0]:         # 정답에서 비교 후 현재 값의 간격이 더 작을 경우
                answer = [start, end]                   # 답 갱신하고

            dic[gems[start]] -= 1                       # 딕셔너리 개수 다운

            if dic[gems[start]] == 0:                   # 다운 후 0이 될 경우는
                del dic[gems[start]]                    # key를 삭제처리

            start += 1                                  # start point 증가

    # 인덱스를 0부터 시작했으므로 각 포인터 인덱스를 1씩 늘리기
    answer[0] += 1
    answer[1] += 1

    return answer