import sys

input=sys.stdin.readline

n=int(input())
tree={} # {'A': ['B','C'],'B':['D','.'], ...} 형태

for i in range(n):
    root,left,right = input().strip().split()
    tree[root] = [left,right] # 'A' 안에  ['B', 'C'] 가 담김

# root가 '.'이 아닐때만 수행하고, root는 출력 left는 다시 함수에 넣어 실행시키는 것이 큰 틀
def pre(root): # 전위
    if root != '.':
        print(root, end='') #root
        pre(tree[root][0]) #left
        pre(tree[root][1]) #right

def ino(root): #중위
    if root != '.':
        ino(tree[root][0])
        print(root, end='') #root
        ino(tree[root][1])

def post(root): #후위
    if root != '.':
        post(tree[root][0])
        post(tree[root][1])
        print(root,end='') # root

pre('A') #root에 'A'를 넣어줌
print()
ino('A')
print()
post('A')