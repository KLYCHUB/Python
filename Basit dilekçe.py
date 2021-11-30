dilekce = ("""
adiniz: {}
soyadiniz: {}
kayit tarihi: {}/{}/{}
""")

ad = str(input("Adinizi girininiz: "))
soyad = str(input("Soyadinizi girininiz: "))
gün = int(input("Kayit aldugunuz gunu giriniz: "))
ay = int(input("Kayit aldugunuz ayi giriniz: "))
yil = int(input("Kayit aldugunuz yili giriniz: "))

print("\n--------------------------------------\n")
print("Dilekçeniz: ",dilekce.format(ad,soyad,gun,ay,yil))
