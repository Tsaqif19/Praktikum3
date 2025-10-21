nama = "Yharis Arkan Tsaqif"
print (f"Nama Saya, {nama}")

a = int(input("masukan bilangan pertama = "))
b = int(input("masukan bilangan kedua   = " ))
c = int(input("masukan bilangan ketiga  = " ))

if a > b and a > c:
    print("bilangan terbesar =",a)
elif b > c:
    print("bilangan terbesar =",b)
else:
    print("bilangan terbesar =",c)

