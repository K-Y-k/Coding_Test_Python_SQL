# 제출한 학생 번호를 리스트로 담고
# N명의 학생을 차례로 조회하면서
# 제출한 리스트 안에 해당 학생이 없으면 정답에 넣기

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    submit_li = list(map(int, input().split()))
    
    answer = []
    
    for i in range(1, N+1):
        if i not in submit_li:
            answer.append(i)
            
    print('#' + str(test_case), ' '.join(map(str, answer)))