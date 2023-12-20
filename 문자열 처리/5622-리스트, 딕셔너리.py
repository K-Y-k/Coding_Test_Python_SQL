# 내가 푼 방식
# 딕셔너리로 각 단어에 따른 걸리는 시간(초)를 지정한 후
# 문제에 주어진 단어를 조회하여 단어에 따른 시간(초)에 +1초를 추가하여 답에 적용했다. 

s = input()

dial_dic = {'A':2, 'B':2, 'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,
            'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,
            'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9}
answer = 0

for i in s:
    answer += dial_dic[i] + 1

print(answer)



# 리스트로 활용한 방식
# 다이얼에 따른 문자들을 리스트에 저장한 후
# 문제에 주어진 단어를 조회와 리스트를 이중 조회하면서 해당 단어가 조회한 리스트의 원소값에 있으면
# 현재 리스트의 원소값의 인덱스 값에 리스트의 인덱스는 0부터 시작했기에 +1에 숫자 1이 2초 걸리므로 +2초까지 더해준다.

s = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

answer = 0

for i in s:
    for j in dial:
        if i in j:
            answer += (dial.index(j) + 1) + 2

print(answer)
