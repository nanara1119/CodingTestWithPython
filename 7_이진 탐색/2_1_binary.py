'''
5
8 3 7 9 2
3
5 7 9
'''

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

n = int(input())
have_array = list(map(int, input().split()))
m = int(input())
target_array = list(map(int, input().split()))

have_array.sort()

for i in target_array:
    result = binary_search(have_array, i, 0, n - 1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
