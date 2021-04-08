'''
5
8 3 7 9 2
3
5 7 9
'''

n = int(input())
have_set = set(map(int, input().split()))

m = int(input())
target_list = list(map(int, input().split()))

for i in target_list:
    if i in have_set:
        print("yes", end=' ')
    else:
        print("no", end=' ')


