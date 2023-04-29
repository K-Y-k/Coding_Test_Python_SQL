# C의 범위가 (3 ≤ L ≤ C ≤ 15)이므로 범위가 넓지 않아서
# 이 문제는 선택의 방법으로 풀 수 있다.
# 알파벳이 코드에 포함할 것인지 말 것인지 2가지의 선택이 있어 2^C개로 최대 2^15까지로 범위가 작아서 브루트포스 방식이 아근ㅇ하다.

# 이 문제의 핵심 포인트 
# 1.암호를 선택하는 재귀 함수 매개변수 선언 잘하기
#   (문제에서 원하는 암호의 최종 길이, 암호에 들어갈 수 있는 알파벳 리스트, 현재까지 온 암호, 인덱스)
# 2.문제에서 모음(최소2개) 자음(최소1개) 개수 체크하라고 했으므로 check함수를 만들어 최종 길이에 왔어도 check함수로 검사해야함 
# 3. 문제에서 암호가 증가하는 순서대로 배열되었다고 했으므로 암호 확인 함수 시작 전 알파벳 리스트를 오름차순으로 정렬해야함


def next_code(finalCode_length, alpha, current_code, index): # 암호 확인 함수
    if len(current_code) == finalCode_length:  # 최종 암호 길이에 도달했을 때
        if check(current_code):                # 모음(최소1개) 자음(최소2개) 개수 체크를 하고
            print(current_code)                # 참이면 출력 후 반환
        return 
    elif index >= len(alpha):                  # 인덱스가 주어진 알파벳 리스트의 인덱스를 벗어난 경우는
        return                                 # 불가능한 경우로 그냥 반환
    else:                                      # 다음 암호를 더 확인해야하는 경우는
        next_code(finalCode_length, alpha, current_code+alpha[index], index+1) # 다음 암호를 선택한 경우 재귀 호출
        next_code(finalCode_length, alpha, current_code, index+1)              # 다음 암호를 선택하지 않은 경우 재귀 호출

    
def check(current_code):                      # 모음 자음 최소 개수 검사 함수
    mo = 0                                    # 모음 자음 개수 초기화
    ja = 0
    
    for i in current_code:                    # 현재 받아온 암호의 알파벳을 하나씩 조회해서
        if i in 'aeiou':                      # 모음이면 모음 카운트 증가
            mo += 1
        else:                                 # 자음이면 자음 카운트 증가
            ja += 1
            
    if mo >= 1 and ja >= 2:                   # 모음 최소 1개이상, 자음 최소 2개이상이면 참 반환
        return True                
    else:
        return False

    
L, C = map(int, input().split())              # 최종 암호 길이, 주어진 알파벳 개수 입력
alpha = list(map(str, input().split()))       # 주어진 알파벳 입력
alpha.sort()                                  # 문제에서 암호가 증가하는 순서대로 배열되었다고 했으므로 오름차순 정렬 후
next_code(L, alpha, "", 0)                    # 처음은 현재 암호가 아무것도 안들어간 상태에서 진행