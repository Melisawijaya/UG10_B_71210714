bil1 = float(input("Masukkan bilangan pertama: "))
bil2 = float(input("Masukkan bilangan kedua: "))
str = str(input("Masukkan kalimat: "))

str = str.lower() # jaga-jaga jika case "Tambahkan kedua bilangan diatas"

if ("kali" in str) :
    hasil = bil1 * bil2
    operator = "perkalian"
elif ("bagi" in str) :
    hasil = bil1 / bil2
    operator = "pembagian"
elif ("tambah" in str) :
    hasil = bil1 + bil2
    operator = "penjumlahan"
elif ("kurang" in str) :
    hasil = bil1 - bil2
    operator = "pengurangan"


print ("hasil %s %s dengan %s adalah %s" % (operator, bil1, bil2, hasil))
 