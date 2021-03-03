N, M = map(int, input().split())

max_num = -1
for i in range(N):
    line = list(map(int, input().split()))
    line_min = min(line)

    max_num = max(max_num, line_min)

print(max_num)
