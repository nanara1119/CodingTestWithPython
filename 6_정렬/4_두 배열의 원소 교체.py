'''
    5 3
    1 2 5 4 3
    5 5 6 6 5
'''

N, K = map(int, input().split())

first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

first_list.sort()
second_list.sort(reverse=True)

for i in range(K):
    if first_list[i] > second_list[i]:
        break
    first_list[i], second_list[i] = second_list[i], first_list[i]


print(sum(first_list))