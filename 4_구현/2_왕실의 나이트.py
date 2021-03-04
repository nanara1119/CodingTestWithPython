max_size = 8
x, y = list(map(str, input()))

x = int(ord(x)) - int(ord('a')) + 1
y = int(y)

dir = [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
count = 0

for dy, dx in dir:
    next_x = x + dx
    next_y = y + dy

    if (0 < next_x <= max_size) and (0 < next_y <= max_size):
        count += 1

print(count)

