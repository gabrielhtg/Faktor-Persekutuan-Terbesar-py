import os

os.system('clear||cls')

n1 = int(input("Masukkan angka pertama  : "))
n2 = int(input("Masukkan angka kedua    : "))

# ! Cek apakah n1 atau n2 yang lebih besar
if (n1 >= n2) == True :
    for i in range(1, n2) :
        if (n1 % i == 0) and (n2 % i == 0) :
            gcd = i

else :
    for i in range(1, n1) :
        if (n1 % i == 0) and (n2 % i == 0) :
            gcd = i

print(f"FPB dari {n1} and {n2} adalah {gcd}")