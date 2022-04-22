import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False]*M for _ in range(N)]
que = deque([[0, 0, 1]])
while que:
    x, y, cnt = que.popleft()
    if x == N-1 and y == M-1:
        print(cnt)
        break
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if grid[nx][ny] == '1':
                visited[nx][ny] = True
                que.append([nx, ny, cnt+1])

