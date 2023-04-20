def solution(numbers, k):
    answer = 0
    index = 0
    
    for i in range(k-1):
        index += 2
        index %= len(numbers)
        
    return numbers[index]