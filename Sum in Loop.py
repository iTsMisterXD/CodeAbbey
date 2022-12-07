bdata = int(input())
data = list(map(int, input().split()))
hasil = 0
for x in range(bdata):
    hasil = hasil + data[x]
print(hasil)
