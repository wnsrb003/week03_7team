import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

discovered = [V]
def dfs(v):
    for w in graph[v]:
        if w not in discovered:
            discovered.append(w)
            dfs(w)

dfs(V)
print(*discovered)


def bfs(V):
    discovered = [V]
    que = deque([V])
    while que:
        v = que.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                que.append(w)

    return discovered

print(*bfs(V))