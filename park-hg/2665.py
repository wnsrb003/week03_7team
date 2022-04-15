import sys
from collections import deque
sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False]*n for _ in range(n)]
visited[0][0] = True
que = deque([[0, 0, 0]])

ans = 1e9
while que:
    x, y, cnt = que.popleft()
    if x == n-1 and y == n-1:
        ans = min(ans, cnt)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            if grid[nx][ny] == '1':
                que.appendleft([nx, ny, cnt])
            else:
                que.append([nx, ny, cnt+1])

print(ans)