def solution(numbers):
    answer = []
    
    if len(numbers) == 2:
        answer.append(numbers[0] * numbers[1])
    else:
        for i in range(len(numbers)):
            for j in range(1, len(numbers)):
                if i != j:
                    answer.append(numbers[i]*numbers[j])

    answer = max(answer)
    
    return answer