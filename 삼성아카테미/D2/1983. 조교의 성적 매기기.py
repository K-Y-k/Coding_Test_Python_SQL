# 문제에서 주어지는 등급을 리스트에 저장한 후
# 각 학생의 성적을 문제에서 주어진 식으로 최종 성적 값을 저장하고
# 성적순으로 정렬할 것이기에 문제에서 원하는 학생 점수를 변수에 따로 저장한 후에 정렬한다.
# 문제에서 N은 10의 배수인 조건이라 N/10명의 학생들에게 동일한 평점을 부여한다고 했으므로 기준치 설정한 후
# 기준치로 나눈 것이 원하는 학생의 성적 인덱스 위치이다.

T = int(input())

grade_li = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    
    total_li = []
    
    for _ in range(N):
        a, b, c = map(int, input().split())
        total = a * 0.35 + b * 0.45 + c * 0.2
        
        total_li.append(total)
        
    k_score = total_li[K-1]
    
    total_li.sort(reverse=True)
    

    # 여기부터 이해를 못하였음 
    div = N // 10                                   # N은 10의 배수인 조건이라 N/10명의 학생들에게 동일한 평점을 부여한다고 했으므로 기준치 설정

    final_k_score = total_li.index(k_score) // div  # 기준치로 나눈 것이 K학생의 평점 위치
    
    print('#' + str(test_case), grade_li[final_k_score])