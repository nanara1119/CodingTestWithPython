N, K = map(int, input().split())

count = 0
while True:
    if N % K == 0:
        N /= K
        count += 1
    elif N != 1:
        N -= 1
        count += 1
    else:
        print(count)
        break



