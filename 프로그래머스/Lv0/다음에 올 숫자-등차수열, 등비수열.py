# 등차수열 : 각 항이 그 앞의 항에 일정한 수를 더한 것으로 이루어진 수열
# 등비수열 : 각 항이 그 앞의 항에 일정한 수를 곱한 것으로 이루어진 수열


# 내가 푼 방식
# 등차수열은 같은 숫자의 간격만큼이므로 각 인덱스의 차이를 저장한 리스트를 만들어서
# 등차수열인지 검증하고 등차수열이면 가장 마지막 값에 그 간격만큼 더한 것을 정답에 넣고
# 등차수열이 아니면 아니면 등비수열이므로 첫항과 2번째항의 등비를 적용하였다.


def solution(common):
    answer = 0

    a = []                                 # 각 인덱스의 차이를 저장한 리스트를 만들어서
    for i in range(len(common)-1):
        a.append(common[i+1] - common[i])

    
    if a[0] == a[1]:                       # 등차수열인지 검증하고 등차수열이면 가장 마지막 값에 그 간격만큼 더한 것을 정답에 넣고
        answer = common[-1] + a[0]
    else:                                  # 등차수열이 아니면 아니면 등비수열이므로 첫항과 2번째항의 등비를 가장 마지막 값에 적용하고 정답에 넣었다.
        b = common[1] / common[0]
        answer = common[-1] * b
    
    
    return answer