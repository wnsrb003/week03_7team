import sys
from collections import defaultdict
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)
def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w)

dfs(1)
print(sum(visited)-1)