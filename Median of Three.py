bdata = int(input())
hasil = []
for i in range(bdata):
    data = list(map(int, input().split()))
    urut = sorted(data)
    hasil.append(urut[1])
print(*hasil, sep=' ')
