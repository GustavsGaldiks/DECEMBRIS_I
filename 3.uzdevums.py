skaitlis=int(input("uzraksti sk.: "))
rez = "nepāra" if skaitlis %2 !=0 else "pāra"
print(f"{skaitlis} ir {rez} skaitlis")