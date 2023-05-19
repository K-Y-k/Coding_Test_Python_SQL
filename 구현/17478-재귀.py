# (현재 진행된 횟수) x ("___")로 구분지었다.

# 재귀 호출이 될 때마다 count(현재 진행된 횟수)에 +1을 하면서,
# 최종 입력했던 물어본 수와 일치해지면, 최종 대답을 1번하고 return 처리하여 재귀를 종료시킨다.

# "라고 답변하였지" 부분은 최근순으로 출력되기에 각 문장이 나오는 순서를 잘 파악하고 재귀를 넣어야한다.



# 내가 푼 방식
def self_function_answer(count):                                   # 최종 1번의 대답을 위한 함수 따로 선언
    print("____"*count + '"재귀함수가 뭔가요?"')
    print("____"*count + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    print("____"*count + "라고 답변하였지.")

def self_function(count, total_count):                             # 반복 질문의 대답하는 함수 선언(현재 반복된 수, 최종 물어본 개수)를 매개변수로 활용
    if count == total_count:                                       # 현재 반복된 수가 최종 입력했던 물어본 수와 동일하면
        self_function_answer(count)                                # 최종 1번의 대답 후
        return                                                     # 반환 처리하여 재귀 끝 맺음
    
    # 현재 반복된 수가 최종 물어본 수가 아니면 재귀 대답 진행
    print("____"*count + '"재귀함수가 뭔가요?"')
    print("____"*count + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print("____"*count + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print("____"*count + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    
    self_function(count+1, total_count)           # 재귀 호출    

    print("____"*count + "라고 답변하였지.")       # 이 답변은 최근 순으로 출력되므로 재귀 후에 넣음


N = int(input())                                  # 최종 물어본 수 입력
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.") 
self_function(0, N)                               # 처음 대답은 ___가 없으므로 count를 0으로 넣고 시작 



# 좀 더 정돈 된 방식
def self_function(count, total_count):
    print("____"*count + '"재귀함수가 뭔가요?"')
    
    if count == total_count:
        print("____"*count + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print("____"*count + "라고 답변하였지.")
        return
    
    print("____"*count + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print("____"*count + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print("____"*count + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    
    self_function(count+1, total_count)

    print("____"*count + "라고 답변하였지.")

N = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
self_function(0, N)