import sys

N = int(input())                                                         # 노드 개수 입력
tree = {}                                                                # 트리를 딕셔너리로 선언

for _ in range(N):                                                       # 노드 개수 만큼 반복
    root, left, right = map(str, sys.stdin.readline().rstrip().split())  # 루트, 왼쪽, 오른쪽 입력 
    tree[root] = [left, right]                                           # 딕셔너리인 트리의 루트에 따른 왼쪽, 오른쪽 노드를 넣는다.
    
def preorder(root):                                                      # 전위 순회 : 루트 -> 왼쪽 자식 -> 오른쪽 자식 순으로 탐색
    if root != '.':                                                       
        print(root, end='')                                              
        preorder(tree[root][0])                                          
        preorder(tree[root][1])
        
def inorder(root):                                                       # 중위 순회 : 왼쪽 자식 -> 루트 -> 오른쪽 자식 순으로 탐색
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])
        
def postorder(root):                                                     # 후위 순회 : 왼쪽 자식 -> 오른쪽 자식 -> 루트 순으로 탐색
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')
        
        
preorder('A')                                                            # 문제에서 A노드부터 탐색을 진행한다고 했으므로
print()
inorder('A')
print()
postorder('A')