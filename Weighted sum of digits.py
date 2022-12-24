bdata = int(input())
hasil = []
data = list(map(str, input().split()))
for i in range(bdata):
    m = list(data[i])
    jmlh = 0
    kali = 1
    for j in range(len(m)):
        jmlh = jmlh + (int(m[j])*(kali))
        kali += 1
    hasil.append(jmlh)
print(*hasil, sep=' ')
