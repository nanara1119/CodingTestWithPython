'''
    2
    홍길동 95
    이순신 77
'''

N = int(input())

s_list = []

for i in range(N):
    line = input().split()
    s_list.append((line[0], line[1]))

result = sorted(s_list, key= lambda item: item[1])

for i, j in result:
    print(i, end=" ")


