N = int(input())

li = list(map(int, input().split()))

li.sort()

print(li[N//2])