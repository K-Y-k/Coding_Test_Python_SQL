def solution(numbers):
    answer = 0
    
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for index, value in enumerate(num_list):
        numbers = numbers.replace(value, index)
        
    answer = int(numbers)
    
    return answer