#1 gonderilen bir kelimeyi belirtilen kez ekranda gosteren fonksiyonu yaziniz.
def ekranaYazdirma(kelime,tekrar):
    print(kelime*tekrar)

sozcuk=input('kelime giriniz: ')
tekrarSayisi=int(input('tekrar gir: '))
ekranaYazdirma(sozcuk,tekrarSayisi)

#2 kendisine gonderilen sinirsiz sayidaki parametreyi listeye ceviren fonksiyonu yaziniz.
def listeyeEkle(*param):
    liste=[]
    for params in param:
        liste.append(param)
        return liste
    
sonuc=listeyeEkle(10,20,'ahmet','@')
print(sonuc)






    


