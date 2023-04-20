def solution(emergency):
    answer = []
    emergency_dict = {}
    
    emergency_sequence = sorted(emergency, reverse = True)
    
    for i in emergency_sequence:
        emergency_dict[i] = emergency_sequence.index(i)+1
        
        
    for i in emergency:
        answer.append(emergency_dict[i])
        
    return answer