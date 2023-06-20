# 이 문제는 주어진 n의 값보다 크고 이진수의 1의 개수가 서로 동일할 때 정답이므로
# for 루프 조회를 n보다 큰 값부터 시작해서 하나씩 이진변환하면서 개수를 비교하면 된다.  


def solution(n):
    answer = 0
    n_one_count = 0
    
    # 카운트 세기 방법 1 : 이번에 배운 방법
    n_bin = bin(n)[2:]
    n_one_count = n_bin.count("1")
    
    # 카운트 세기 방법 2 : 내가 푼 방식
    # for i in str(n_bin):
    #     if i == "1":
    #         n_one_count += 1
    
    for i in range(n+1, 1000001):
        # 카운트 세기 방법 1의 축소판
        temp_one_count = bin(i).count("1")
        
        if temp_one_count == n_one_count:
            answer = i
            break
    
    return answer