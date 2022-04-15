import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)

from collections import deque, defaultdict

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
visited = [False] * (N+1)

graph = defaultdict(list)
for _ in range(1, M+1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True
    cnt = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                cnt += 1
                visited[i] = True
    return cnt

print(bfs(graph, 1, visited))