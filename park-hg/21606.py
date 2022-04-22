import sys
from collections import defaultdict

sys.stdin = open('input.txt')


N = int(sys.stdin.readline())
A = sys.stdin.readline().rstrip()

graph = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u] += v,
    graph[v] += u,


ans = 0
visited = [False]*(N+1)
def dfs(v):
    cnt = 0
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            if A[w-1] == '1':
                cnt += 1
            else:
                cnt += dfs(w)
    return cnt


for v in range(1, N+1):
    if A[v-1] == '1':
        for w in graph[v]:
            if A[w-1] == '1':
                ans += 1
    else:
        if not visited[v]:
            cnt = dfs(v)
            ans += cnt*(cnt-1)
        

print(ans)