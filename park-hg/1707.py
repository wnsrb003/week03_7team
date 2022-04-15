import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')


def bfs():
    parity = [0]*(V+1)
    for v in range(V+1):
        if parity[v] == 0:
            parity[v] = 1
            que = deque([v])
            while que:
                v = que.popleft()
                for w in graph[v]:
                    if parity[w] == 0:
                        parity[w] = -parity[v]
                        que.append(w)
                    else:
                        if parity[w] == parity[v]:
                            print('NO')
                            return

    print('YES')


K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    
    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    bfs()
