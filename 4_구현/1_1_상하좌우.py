N = int(input())
O = list(map(str, input().split()))

X, Y = 1, 1

def check_location(x, y):
    if (N >= x >= 1) and (N >= y >= 1):
        return True
    return False

for n in O:
    if n is 'L':
        if check_location(Y, X - 1):
            X -= 1
    elif n is 'R':
        if check_location(Y, X + 1):
            X += 1
    elif n is 'U':
        if check_location(Y - 1, X):
            Y -= 1
    elif n is 'D':
        if check_location(Y + 1, X):
            Y += 1
print(Y, X)

