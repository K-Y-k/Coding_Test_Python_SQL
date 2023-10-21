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