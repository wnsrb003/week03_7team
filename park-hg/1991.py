import sys
from collections import defaultdict
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

graph = defaultdict(list)
for _ in range(N):
    root, left, right = sys.stdin.readline().rstrip().split()
    graph[root].append(left)
    graph[root].append(right)

def preorder(v):
    if graph[v]:
        left, right = graph[v]
        print(v, end='')
        preorder(left)
        preorder(right)
        
def inorder(v):
    if graph[v]:
        left, right = graph[v]
        inorder(left)
        print(v, end='')
        inorder(right)

def postorder(v):
    if graph[v]:
        left, right = graph[v]
        postorder(left)
        postorder(right)
        print(v, end='')
        

preorder('A')
print('')
inorder('A')
print('')
postorder('A')
print('')