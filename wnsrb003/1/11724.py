import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

from collections import defaultdict
graph = defaultdict(list)

for i in range(1,M+1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
cnt = 0
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

for i in range(1,N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt+=1
print(cnt)