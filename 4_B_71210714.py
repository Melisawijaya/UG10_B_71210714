angka = int(input("Masukkan angka: "))

#rumus
if ((angka % 2) == 0) and ((angka % 3) != 0) :
    jawab = "YA"
elif ((angka % 2) != 0) and ((angka % 3) == 0) :
    print ("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")
    exit();

print ("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: ", jawab)

print ("")

if ((angka % 5) != 0) or ((angka % 10) == 0) :
    jawab = "IYA DONG"
elif ((angka % 5) == 0) or ((angka % 10) != 0) :
    jawab = "TIDAK"

print ("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: ", jawab)
