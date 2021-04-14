'''
4
1 3 1 5
'''

N = int(input())
M = list(map(int, input().split()))

d = [0] * 100

d[0] = M[0]
d[1] = max(M[1], d[0])

for i in range(2, N):
    d[i] = max(d[i - 2] + M[i], d[i - 1])

print(d[N-1])


