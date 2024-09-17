def cumleYazdirma ():         #def ile fonksiyon tanimlanir. 
    print('merhaba dunya!') 

cumleYazdirma()
          

def cumleYazdirma2 (isim):
    print('merhaba '+isim)

cumleYazdirma2('ahmet') 

def cumleYazdirma3(isim2):
    return 'merhaba '+isim2

print('mehmet')

def toplama(sayi1,sayi2):  #toplam sonucu return edilerek ekrana yazdirildi.
    return sayi1+sayi2

sonuc=toplama(1,3)
print(sonuc)

def yasHesaplama (dogumYili):
    return 2024-dogumYili

sonuc2=yasHesaplama(int(input('dogum yiini giriniz: ')))
print(sonuc2)


