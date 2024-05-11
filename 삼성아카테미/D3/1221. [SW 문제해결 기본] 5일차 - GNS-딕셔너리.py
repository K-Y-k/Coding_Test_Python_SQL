# 문제에서 각 숫자를 정의한 문자를 딕셔너리에 정의해준 후
# 오름차순으로 다시 출력하려는 것이므로
# 0부터 9순서대로 주어진 문장에서의 각 숫자 문자의 개수를 파악한 후 
# 정답에 찾은 숫자의 문자를 개수만큼 넣어주면 오름차순 형태로 다시 만들 수 있다.

num_dic = {0:'ZRO', 1:'ONE', 2:'TWO', 
           3:"THR", 4:"FOR", 5:"FIV", 
           6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}


tc, tc_len = map(str, input().split())
num_li = list(map(str, input().split()))     # 주어진 문장
answer = []


for i in range(10):                          # 0부터 9순서대로
    find_count = num_li.count(num_dic[i])    # 주어진 문장에서의 각 숫자 문자의 개수를 파악한 후 

    for _ in range(find_count):              # 정답에 찾은 숫자의 문자를 개수만큼 넣어주면 오름차순 형태로 다시 만들 수 있다.
        answer.append(num_dic[i])


print(tc)
print(' '.join(map(str,answer)))