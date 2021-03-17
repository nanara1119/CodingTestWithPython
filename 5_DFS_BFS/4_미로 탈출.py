'''
5 6
101010
111111
000001
111111
111111

3 3
110
010
011
'''
from collections import deque

N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input())))

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        iy, jx = queue.popleft()

        for c in range(4):
            ny = iy + dy[c]
            nx = jx + dx[c]

            if not(0 <= ny < N) or not(0 <= nx < M):
                continue

            if maze[ny][nx] == 0:
                continue

            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[iy][jx] + 1
                queue.append((ny, nx))

    return maze[N-1][M-1]

print(bfs(0, 0))

