sk=int(input("uzraksti sk.: "))
rez = 1
for i in range (1, sk + 1):
    rez*=i
print(f"Faktoriāls no {sk} ir {rez}")