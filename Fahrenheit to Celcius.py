data = list(map(int, input().split()))
hasil = []
for x in range(data[0]):
    c = round((data[x+1]-32)*(5/9)+0.0001)
    hasil.append(c)
print(*hasil)
