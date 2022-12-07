bdata = int(input())
hasil = []
for x in range(bdata):
    x, y = list(map(int, input().split()))
    hasil.append(x+y)
print(*hasil)
