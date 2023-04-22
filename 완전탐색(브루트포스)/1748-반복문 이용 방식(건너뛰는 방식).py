N = int(input())
result = 0
start = 1                            # 시작값 초깃값 지정
length = 1                           # 자릿수 초깃값 지정

while start <= N:
    end = start*10-1                 # 끝의 값은 동일한 자릿수의 마지막으로 9 99 999 999같이 시작 값*10-1로 구해준다.
    
    if N < end:                      # N의 값이 마지막 값이므로 갱신된 자릿수의 마지막 값보다 작을 때   
        end = N                      # 예외처리로 끝의 값을 N으로 변경해야한다.
        
    result += (end-start+1)*length   # 각 자릿수 개수에 따른 공식을 적용하여 더해주고
    
    start *= 10                      # 시작 값은 자릿수가 바뀔때의 첫값으로 1 10 100 1000같이 10씩 곱해주면된다.
    length += 1
    
print(result)                        # 모든 반복을 거친 후의 최종 자릿수 총 개수를 출력
