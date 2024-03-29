import sys

N = int(input())                                                   # 반복할 개수 입력

words = []                                                         # 단어 저장 리스트
alpha_dict = {}                                                    # 입력된 단어에 맞는 매칭되는 숫자를 넣을 딕셔너리
num_list = []                                                      # 위 매칭된 숫자를 내림차순으로 정렬하기위해 숫자만 넣을 리스트

for _ in range(N):                                                 # N번 만큼의 단어 입력
    words.append(sys.stdin.readline().rstrip())
    
for i in range(N):                                                 # N번의 단어를 가져오고
    for j in range(len(words[i])):                                 # N번째 단어의 각 자리수의 알파벳을 가져와서 딕셔너리에 숫자 넣어주기
        if words[i][j] in alpha_dict:                              # 딕셔너리에 이미 해당 알파벳이 있으면 
            alpha_dict[words[i][j]] += 10 ** (len(words[i])-j-1)   # -j-1로 각 자릿수에 맞게 표현
        else:                                                      # 없으면 새로 넣어준다.
            alpha_dict[words[i][j]] = 10 ** (len(words[i])-j-1)            
    
for i in alpha_dict.values():                                      # 딕셔너리에 넣은 값들을 숫자 리스트로 다시 넣어주고
    num_list.append(i)
    
num_list.sort(reverse=True)                                        # 내림차순으로 정렬


max_result = 0                                                     # 최종 최대 결과 값 변수
num = 9                                                            # 알파벳에 따른 곱할 숫자

for i in num_list:                                                 # 제일 높은 값 순서이므로 높은 수인 9부터 순차적으로 곱한 값을 계속 더해줌
    max_result += num * i
    num -= 1
    
print(max_result)
    
    