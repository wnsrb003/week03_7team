import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

N, M, K, X = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

que = deque([[X, 0]])
visited = [False]*(N+1)
visited[X] = True
ans = []
while que:
    v, cnt = que.popleft()
    if cnt == K:
        ans.append(v)

    for w in graph[v]:
        if not visited[w]:
            visited[w] = True
            que.append([w, cnt+1])

ans.sort()

if not ans:
    print(-1)
else:
    for v in ans:
        print(v)