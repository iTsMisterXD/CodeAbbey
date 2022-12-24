import math
bdata = int(input())
hasil = []
for x in range(bdata):
    data = input()
    dadu = math.floor(float(data)*6)+1
    hasil.append(dadu)
print(*hasil)
