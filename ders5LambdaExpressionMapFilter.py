def kareAlma(sayi):
    return sayi**2

sonuc=kareAlma(2)
print(sonuc)
#map butun diziyi isleme sokar.
sayilar=[1,2,3,4]
sonuc2=list(map(kareAlma,sayilar)) #liste icindeki elemanlari tek tek foksiyona sokar

print(sonuc2)

cevreHesabi=lambda sayi2:sayi2**2 #tek seferlik diziyi fonksiyona sokar
sonuc3=list(map(cevreHesabi,sayilar))

sonuc4=list(filter(lambda sayi4:sayi4%2==0,sayilar)) #sadece cift olanlari filtreledi.
print(sonuc4)