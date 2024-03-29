def sol_dynamic(n) :       # 점화식을 활용한 다이나믹 함수 선언
    if n == 1 :            # d[1]은 1
        return 1

    elif n == 2 :          # d[2]는 2
        return 2
    
    elif n == 3 :          # d[3]은 3
        return 4
    
    else :                 # 그 이후 값들은 재귀 호출 방식으로 위 d[1],d[2],d[3]의 값을 활용하여 구해진다.
        return sol_dynamic(n-1) + sol_dynamic(n-2) + sol_dynamic(n-3)

T = int(input())           # 입력 횟수 선언
 
for _ in range(T) :        # 입력 횟수 만큼의 값 입력 및 결과 출력
    n = int(input())   
    print(sol_dynamic(n))





# d[n] = n을 1,2,3의 합으로 나타내는 방법의 수로                                 
# a1 + a2+ a3+... + ax = n이고 마지막 수 ax는 1,2,3만 들어갈 수 있으므로
#        n-1      + 1  = n  => 1의 합으로 나타내는 방법의 수
#        n-2      + 2  = n  => 2의 합으로 나타내는 방법의 수
#        n-3      + 3  = n  => 3의 합으로 나타내는 방법의 수
# 의 형태로 표현이 가능해진다.
# 이 외의 방법은 없으니 위의 각 경우의 수를 더하면 되는 것이다.
# 즉, 점화식은 d[n] = d[n-1] + d[n-2] + d[n-3]이다.
