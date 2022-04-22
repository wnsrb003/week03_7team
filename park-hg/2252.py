import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
indegree = [0]*(N+1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1

que = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        que.append(i)

discovered = []
while que:
    v = que.popleft()
    discovered.append(v)
    for w in graph[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            que.append(w)

print(*discovered)