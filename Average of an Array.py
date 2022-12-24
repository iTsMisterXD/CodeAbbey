bdata = int(input())
hasil = []
for i in range(bdata):
    data = list(map(int, input().split()))
    sum = 0
    for j in range(len(data)-1):
        sum = sum + data[j]
    hasil.append(sum/(len(data)-1))
print(*hasil, sep=' ')
