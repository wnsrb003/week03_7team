# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현(2차원 리스트)
# graph = [
#     [],
#     [2,3,8], # 1번 노드와 연결
#     [1,7], # 2번 노드와 연결
#     [1,4,5], # ...
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)


from collections import deque
import sys
# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현(2차원 리스트)
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

from collections import defaultdict

sys.stdin = open('input.txt')

N, M, V = list(map(int, sys.stdin.readline().strip().split()))
graph = defaultdict(list)
# graph = {(i+1): [] for i in range(N)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph.keys():
    graph[i].sort()
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * (N+1)

# 정의된 DFS 함수 호출
dfs(graph, V, visited)
print()
visited = [False] * (N+1)

# 정의된 DFS 함수 호출
bfs(graph, V, visited)