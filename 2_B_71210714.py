RSI = int(input("Masukkan besar RSI: "))
MACD = str(input("Masukkan kondisi MACD: "))
MACD = MACD.lower() #jaga-jaga jika input MACD menggunakan upper case"

if(RSI>=70):
    sinyalRsi = 1
    strRsi = "RSI lebih dari sama dengan 70"
elif(RSI<=30):
    sinyalRsi = 2
    strRsi = "RSI kurang dari sama dengan 30"
elif(RSI>30 and RSI<70):
    sinyalRsi = 0
    strRsi = "RSI berada di area 31 - 69"

if(MACD == "golden-cross"): 
    sinyalMacd = 1
    strMacd = "MACD Golden-cross"
elif(MACD == "death-cross"):
    sinyalMacd = 2
    strMacd = "MACD Death-cross"

if(sinyalRsi == 1 and sinyalMacd == 1):
    strKeputusan = "Tunggu MACD sampai Death-cross"
elif(sinyalRsi == 1 and sinyalMacd == 2):
    strKeputusan = "Saatnya jual"
elif(sinyalRsi == 2 and sinyalMacd == 1):
    strKeputusan = "Saatnya beli"
elif(sinyalRsi == 2 and sinyalMacd == 2):
    strKeputusan = "Tunggu MACD sampai Golden-cross"
elif(sinyalRsi == 0):
    strKeputusan = "Bukan saatnya membeli ataupun menjual"

print(strRsi + " dan " + strMacd + ", " + strKeputusan)

