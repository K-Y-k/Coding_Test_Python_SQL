# 입력한 문자를 하나씩 가져와서
# L일 때와 R일 때의 각 케이스에 맞는 연산을 적용해주면 된다.

command = str(input())

tree = [1, 1]

for i in command:
    if i == 'L':
        tree[1] += tree[0]
    else:
        tree[0] += tree[1]

print(tree[0], tree[1])