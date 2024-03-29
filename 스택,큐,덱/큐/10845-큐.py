import sys

n = int(input())                   # 입력 횟수 선언
queue = [0]*n                      # 입력 횟수 만큼의 크기 지정 = 사용할 큐의 크기만큼 미리 확보해야함
begin = 0                          # 시작 끝 초기화
end = 0

for _ in range(n):
    cmd, *val = sys.stdin.readline().split() # 명령어와 숫자 입력, *val의 *은 가변적으로 할당할 때 사용
    
    if cmd == 'push':             # 정수 X를 큐에 넣는 연산
        num = int(val[0])         # 문자형으로 입력되었기에 넣는 값은 정수형으로 변환
        queue[end] = num          # 끝에 값 삽입
        end += 1                  # end 1칸 증가
         
    elif cmd == 'pop':
        if begin == end:
            print(-1)
        else:
            print(queue[begin])   # 앞의 값 출력
            queue[begin] = 0 
            begin += 1            # begin 1칸 증가
    
    elif cmd == 'size':
        print(end-begin)          # 크기는 끝 - 시작
    
    elif cmd == 'empty':
        if begin == end:          # 비어있으면 1출력
            print(1)
        else:
            print(0)
    
    elif cmd == 'front':
        if begin == end:
            print(-1)
        else:
            print(queue[begin])   # 가장 앞에 있는 값 출력
        
    elif cmd == 'back':
        if begin == end:
            print(-1)
        else:
            print(queue[end-1])   # 인덱스 범위는 0부터 end-1이기 때문에
