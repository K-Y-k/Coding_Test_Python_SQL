P, K = map(int, input().split())

count = 1

for i in range(K, 1000):
    if i == P:
        print(count)
        
    count += 1