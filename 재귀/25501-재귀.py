# 재귀를 활용한 팰린드롬인지 판별하는 함수가 C언어로 주어져있어
# 파이썬으로 변형했고 여기서 추가로 요구하는 내용은 recursion 함수가 몇변 호출했는지이므로
# 추가로 count 인자를 추가하여 여기에 recursion 함수가 호출될 때마다 카운팅했다.
# 반환할 때 배열 형태로 count 값까지 같이 반환하여 출력했다.
 
import sys

def recursion(s, l, r, count):
    count += 1

    if l >= r:
        return [1, count]
    elif s[l] != s[r]:
        return [0, count]
    else:
        return recursion(s, l+1, r-1, count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, count)


N = int(input())

for _ in range(N):
    word = sys.stdin.readline().strip()
    count = 0
    
    answer = isPalindrome(word)

    print(answer[0], answer[1])