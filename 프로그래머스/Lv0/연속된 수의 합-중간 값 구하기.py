# 내가 푼 방식
# 중간 값을 구하고 
# 중간 값에서 제일 앞/뒤의 간격을 구하고
# 이를 이용해 첫 번째 인덱스를 구하여 첫 번째 인덱스부터 문제에서 주어진 연속된 길이까지 정답에 넣어주면 된다


def solution(num, total):
    answer = []
    
    if total % num == 0:                       # 연속된 수의 개수가 홀수인 경우 
        middle_num = total // num              # 중간 값을 구하고 
        cycle_count = (num-1) // 2             # 중간 값에서 제일 앞/뒤의 간격을 구하고
        start = middle_num-cycle_count         # 이를 이용해 첫 번째 인덱스를 구하여

        for i in range(start, start+num):      # 첫 번째 인덱스부터 문제에서 주어진 연속된 길이까지 정답에 넣어주면 된다
            answer.append(i)

    else:                                      # 연속된 수의 개수가 짝수인 경우
        middle_num = total // num
        cycle_count = (num-2) // 2             # 짝수 개수는 중간 값을 제외하면 홀수라서 -2를 해야 제일 앞의 간격을 파악할 수 있다.
        start = middle_num-cycle_count      
        
        for i in range(start, start+num):
            answer.append(i)
    

    return answer