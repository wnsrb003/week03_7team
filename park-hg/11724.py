import sys
from collections import defaultdict
sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False]*N

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w)

ans = 0
for i in range(N):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)