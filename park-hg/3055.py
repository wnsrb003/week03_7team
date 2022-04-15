from copy import deepcopy
import sys
from collections import deque
sys.stdin = open('input.txt')

R, C = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'D':
            end = [i, j]
        elif grid[i][j] == 'S':
            start = [i, j]        

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def kaktus():
    new_grid = deepcopy(grid)
    for x in range(R):
        for y in range(C):
            if grid[x][y] == '*':
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] in ['.', 'S']:
                        new_grid[nx][ny] = '*'

    return new_grid


que = deque([[start[0], start[1], 0]])
visited = [[False]*C for _ in range(R)]
visited[start[0]][start[1]] = True
while que:
    sz = len(que)
    for _ in range(sz):
        x, y, cnt = que.popleft()
        if x == end[0] and y == end[1]:
            print(cnt)
            exit()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if grid[nx][ny] == '.':
                    que.append([nx, ny])
                    visited[nx][ny] = True
        
    grid = kaktus(grid)


