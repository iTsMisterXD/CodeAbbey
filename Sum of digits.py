bdata = int(input())
hasil = []
for x in range(bdata):
    a, b, c = list(map(int, input().split()))
    k = str(a*b+c)
    jmlh = 0
    for y in k:
        jmlh += int(y)
    hasil.append(jmlh)
print(*hasil)
