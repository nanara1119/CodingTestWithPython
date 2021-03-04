I = int(input())

max_count = ((I + 1) * 60 * 60) - 1

count = 0

for i in range(max_count):
    h = int ( i / 60 / 60)
    m = int((i - h * 3600) / 60)
    s = int(i - (h * 3600) - (m * 60))

    number = str(h)+str(m)+str(s)

    if number.count("3"):
        count += 1    
    
print(count)

'''
for i in range(I+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
'''


