from collections import defaultdict, deque
import sys

input=sys.stdin.readline

n,m,v = map(int,input().split())

graph = defaultdict(list) #딕셔너리를 만들어주는 함수 거기에 내가 리스트를 넣는다구,,
for i in range(m): #{1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(v):
    visited[v] =1
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i]=1

def bfs(v):
    q=deque([v])
    visited[v]=1 #true
    while q:
        now = q.popleft()
        print(now,end=' ') #띄어쓰기
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=1 #true

visited = [0]*(n+1) #false
dfs(v)
print()
visited = [0]*(n+1) #false
bfs(v)