import sys
from collections import deque
sys.stdin = open('input.txt')

M, N, H = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

grid = []
for _ in range(H):
    grid.append([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

visited = []
for _ in range(H):
    visited.append([[False]*M for _ in range(N)])

zeros = set()
que = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if grid[i][j][k] == 1:
                que.append([i, j, k, 0])
                visited[i][j][k] = True
            elif grid[i][j][k] == 0:
                zeros.add((i, j, k))

while que:
    x, y, z, cnt = que.popleft()
    for i in range(6):
        nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and not visited[nx][ny][nz]:
            if grid[nx][ny][nz] == 0:
                zeros.remove((nx, ny, nz))
                grid[nx][ny][nz] = 1
                visited[nx][ny][nz] = True
                que.append([nx, ny, nz, cnt+1])

if len(zeros) == 0:
    print(cnt)
else:
    print(-1)