bdata = int(input())
hasil = []
for x in range(bdata):
    s1, s2, s3 = list(map(int, input().split()))
    if s1+s2>=s3 and s2+s3>=s1 and s1+s3>=s2:
        hasil.append('1')
    else:
        hasil.append('0')
print(*hasil)
