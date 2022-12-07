bdata = int(input())
hasil = []
for x in range(bdata):
    kata = str(input().lower())
    k = 0
    for y in range(len(kata)):
        if kata[y] == 'a' or kata[y] == 'o' or kata[y] == 'u' or kata[y] == 'i' or kata[y] == 'e' or kata[y] == 'y':
            k += 1
    hasil.append(k)
print(*hasil)
