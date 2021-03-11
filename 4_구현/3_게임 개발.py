N, M = map(int, input().split())
# 0 - 위, 1 - 오 , 2 - 왼, 3 - 아래
Y, X, D = list(map(int, input().split()))
# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

count = 1

v_map = [[0] * M for _ in range(N)]
v_map[Y][X] = 1
g_map = []
for i in range(N):
    g_map.append(list(map(int, input().split())))

# input end
def turn_left():
    global D
    D -= 1
    if D == -1:
        D = 3

turn_count = 0
while True:
    turn_left()

    next_y = Y + dy[D]
    next_x = X + dx[D]

    # 이동 가능
    if g_map[next_y][next_x] == 0 and v_map[next_y][next_x] == 0:
        v_map[next_y][next_x] = 1
        Y = next_y
        X = next_x
        count += 1
        turn_count = 0
        continue

    # 이동 불가 > 회전만 수행
    else:
        turn_count += 1

    # 한바퀴 회전
    if turn_count == 4:
        next_y = Y - dy[D]
        next_x = X - dx[D]
        if v_map[next_y][next_x] == 0:
            Y = next_y
            X = next_x
        else:
            # 더이상 이동&회전 불가
            break
        turn_count = 0

print(count)

