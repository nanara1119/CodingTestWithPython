# memoization, top-down
# O(N)

d = [0] * 1000

def fibo(x):
    print("fibo({})".format(x))
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(6))