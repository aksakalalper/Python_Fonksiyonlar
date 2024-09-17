def toplama(a,b):
    return sum((a,b)) #sum fonksiyonu gomuludur.

print(toplama(10,20))

def kullaniciBilgileriGoster(**args):

 for key,value in args.items(): 
    print('{} {}'.format(key,value))   #farkli tipteki listeleri ekrana yazdirir
kullaniciBilgileriGoster(isim='ahmet',yas=30,sehir='istanbul')
kullaniciBilgileriGoster(isim='mehmet',yas=22,sehir='izmir',tel='568 586')
kullaniciBilgileriGoster(isim='ayse',yas=19,sehir='kocaeli')

def fonksiyon(x,y,*arguman,**argumanlar):
   print(x)
   print(y)
   print(arguman) #tuple liste oldu
   print(argumanlar) #sozluk oldu
 
fonksiyon(1,2,3,4,deger='alti',deger2='yedi')






