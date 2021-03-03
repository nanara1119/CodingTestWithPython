N, M, K = map(int, input().split())
input_data = list(map(int, input().split()))

input_data.sort(reverse=True)
first = input_data[0]
second = input_data[1]

sum = 0

count = int(M / (K+1)) * K
count += int(M % (K+1))

sum += count * first
sum += (M-count) * second

print(sum)