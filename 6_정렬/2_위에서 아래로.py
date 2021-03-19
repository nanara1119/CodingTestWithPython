N = int(input())

n_list = []

for _ in range(N):
    n_list.append(int(input()))

n_list = sorted(n_list, reverse=True)

for i in n_list:
    print(i , end= " ")




