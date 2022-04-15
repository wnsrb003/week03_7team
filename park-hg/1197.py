import sys
sys.stdin = open('input.txt')

V, E = map(int, sys.stdin.readline().split())

par = list(range(V+1))
rank = [0]*(V+1)

def find(x):
    if x == par[x]:
        return x
    par[x] = find(par[x])
    return par[x]

def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
        return 
    
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def same(x, y):
    return find(x) == find(y)

edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
edges.sort(key=lambda x: x[-1])

ans = 0
for A, B, C in edges:
    if not same(A, B):
        unite(A, B)
        ans += C

print(ans)