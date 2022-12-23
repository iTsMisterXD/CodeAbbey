from collections import Counter
bdata, jumlah = list(map(int, input().split()))
data = list(map(int, input().split()))
hasil = Counter(sorted(data)).values()
print(*hasil)
