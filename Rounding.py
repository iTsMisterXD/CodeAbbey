bdata = int(input())
hasil = []
for x in range(bdata):
    x, y= list(map(int, input().split()))
    hasil.append(round((x/y)+0.0001))
print(*hasil)
