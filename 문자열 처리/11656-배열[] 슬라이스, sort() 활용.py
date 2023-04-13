word = input()

prefix_list = []

for i in range(len(word)):
    prefix_list.append(word[i:])    # 배열 슬라이스로 현재 위치부터 끝까지의 문자를 넣기
    
prefix_list.sort()                  # 오름차순 정렬

for i in prefix_list:
    print(i)