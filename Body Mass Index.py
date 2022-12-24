bdata = int(input())
hasil = []
for x in range(bdata):
    berat, tinggi = list(map(float, input().split()))
    BMI = berat/(tinggi**2)
    if BMI<18.5:
        hasil.append("under")
    elif BMI<25.0 and BMI>18.5:
        hasil.append("normal")
    elif BMI<30.0 and BMI>25.0:
        hasil.append("over")
    elif BMI>30.0:
        hasil.append("obese")
print(*hasil)
