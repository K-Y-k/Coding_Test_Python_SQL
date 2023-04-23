def solution(n):
    answer = 0
    strTointArray = list(map(int, str(n)))
    

    for i in strTointArray:
        answer += i

        print(n)
        print(strTointArray)
            

    return answer