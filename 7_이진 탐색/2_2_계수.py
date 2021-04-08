'''
5
8 3 7 9 2
3
5 7 9
'''

n = int(input())
have_array = [0] * 1000001

for i in input().split():
    have_array[int(i)] = 1

m = int(input())
target_array = list(map(int, input().split()))

for i in target_array:
    if have_array[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end= ' ')

