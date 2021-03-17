'''
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

N, M = map(int, input().split())

ice_map = []
group_count = 0

for _ in range(N):
    ice_map.append(list(map(int, input())))


## dfs
def dfs(i, j):
    if not(0 <= i < N) or not(0 <= j < M):
        return False

    if ice_map[i][j] == 0:
        ice_map[i][j] = 1
        # 상, 하, 좌, 우
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            group_count += 1

print(group_count)
