bdata = int(input())
hasil = []
for x in range(bdata):
    a, b, n = list(map(int, input().split()))
    jmlh = 0
    awal = a
    for y in range(n):
        jmlh = jmlh + awal
        awal += b
    hasil.append(jmlh)
print(*hasil)
