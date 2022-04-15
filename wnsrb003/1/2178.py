import sys
sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  # deque 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # 벽이므로 진행 불가
      if graph[nx][ny] == 0:
        continue
      
      # 벽이 아니므로 이동
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return graph[N-1][M-1]

print(bfs(0, 0))

# from collections import defaultdict, deque

# N, M = map(int, sys.stdin.readline().split())

# miro = [0] * (N*M+1)
# visited = [False] * (N*M+1)

# for j in range(N):
#     temp = list(sys.stdin.readline().strip())
#     for g in range(len(temp)):
#         miro[j*M + g+1] = temp[g]

# graph = defaultdict(list)
# for i in range(1, len(miro)-1):
#     if miro[i] != '0' and miro[i+1] == '1' and i%M != 0: 
#         graph[i].append(i+1)
#         graph[i+1].append(i)

#     if i >= len(miro)-M:
#         continue
    
#     if i%M != 0 and miro[i+M] != '0' and miro[i+M] == '1':
#         graph[i].append(i+M)
#         graph[i+M].append(i)

# def bfs(graph, start, visited):
#     queue = deque([start])
#     cnt = 1
    
#     while queue:
#         v = queue.popleft()
#         visited[v] = True
#         for i in graph[v]:
#             if not visited[i] :
#                 break
#         else :
#             cnt -= 1

#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 cnt += 1

#     return cnt+1
# print(bfs(graph, 1, visited))