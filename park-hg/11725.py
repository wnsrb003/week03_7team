from collections import defaultdict
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

par = [-1]*(N+1)
visited = [False]*(N+1)

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            par[w] = v
            dfs(w)

dfs(1)
for i in range(2, N+1):
    print(par[i])