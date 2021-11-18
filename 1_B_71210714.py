huruf = input("Masukkan nilai huruf PrakTekKom anda: ")
pembatas = ("="*25)
print(pembatas)

#Standar Nilai
if huruf == 'A' :
    nilai = "85 - 100"
elif huruf == 'A-' :
    nilai = "80 - 84"
elif huruf == 'B+' :
    nilai = "75 - 89"
elif huruf == 'B' :
    nilai = "70 - 74"
elif huruf == 'B-' :
    nilai = "65 - 69"
elif huruf == 'C+' :
    nilai = "60 - 64"
elif huruf == 'C' :
    nilai = "55 - 59"
elif huruf == 'D' :
    nilai = "45 - 54"
elif huruf == 'E' :
    nilai = "0 - 44"
else :
    print ("Inputan anda salah atau nilai huruf tidak ada pada Standar Nilai")

if(huruf == 'A' or huruf =='A-' or huruf == 'B+' or huruf == 'B' or huruf == 'B-' or huruf == 'C+' or huruf == 'C' or huruf == 'D' or huruf == 'E'):
    print ("Rentang nilai PrakTekKom anda adalah ", nilai)
