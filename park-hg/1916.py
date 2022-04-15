import sys
import heapq
from collections import defaultdict
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = defaultdict(list)
edge = [[1e10]*(N+1) for _ in range(N+1)]
d = [1e10]*(N+1)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if b not in graph[a]:
        graph[a].append(b)
    edge[a][b] = min(edge[a][b], c)
s, e = map(int, sys.stdin.readline().split())
d[s] = 0
heap = []
heapq.heappush(heap, (0, s))
while heap:
    _, v = heapq.heappop(heap)
    for w in graph[v]:
        if d[w] > d[v] + edge[v][w]:
            d[w] = d[v] + edge[v][w]
            heapq.heappush(heap, (d[w], w))

print(d[e])
