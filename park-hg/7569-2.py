import sys
from collections import deque
sys.stdin = open('input.txt')

M, N, H = map(int, sys.stdin.readline().split())
grid = []
for _ in range(H):
    grid.append([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

visited = []
for _ in range(H):
    visited.append([[-1]*M for _ in range(N)])

que = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if grid[i][j][k] == 1:
                que.append([i, j, k])
                

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while que:
    x, y, z = que.popleft()
    for i in range(6):
        nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and grid[nx][ny][nz] == 0:
                grid[nx][ny][nz] = grid[x][y][z] + 1
                que.append([nx, ny, nz])


ans = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if grid[i][j][k] == 0:
                print(-1)
                exit()
            elif grid[i][j][k] != -1:
                ans = max(ans, grid[i][j][k])

print(ans-1) 
