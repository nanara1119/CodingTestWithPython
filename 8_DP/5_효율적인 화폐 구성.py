'''
3 4
3
5
7

2 15
2
3

'''
N, M = list(map(int, input().split()))
token = []
max = 10001

for i in range(N):
    token.append(int(input()))

dp = [max] * (M + 1)
dp[0] = 0

for i in range(N):
    for j in range(token[i], M + 1):
        if dp[j - token[i]] != max:
            dp[j] = min(dp[j], dp[j - token[i]] + 1)

if dp[M] == max:
    print(-1)
else:
    print(dp[M])
