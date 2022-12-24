bdata = int(input())
jmlh = 0
data = list(map(int, input().split()))
for i in range(bdata):
    jmlh += data[i]
    jmlh *= 113
    jmlh %= 10000007
print(jmlh)
