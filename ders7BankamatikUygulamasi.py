ahmetHesap={
    'isim':'ahmet yilmaz',
    'hesapNo':'11223',
    'bakiye':3000,
    'ekHesap':2000
}
mehmetHesap={
    'isim':'mehmet yilmaz',
    'hesapNo':'445566',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f'Merhaba {hesap['isim']} hosgeldiniz')
    cekilecekMiktar=int(input('cekmek istediginiz para miktarini giriniz: '))
    if (cekilecekMiktar<=hesap['bakiye']):
        print(f'para cekme islemi basarili {hesap['bakiye']}')
    elif((hesap['bakiye']<cekilecekMiktar)):
        if(cekilecekMiktar<=(hesap['bakiye']+hesap['ekHesap'])):
            print(f'para cekme islemi basarili {hesap['bakiye']} ek hesaptan cekildi')
        else:
            print('bakiye yetersiz')
    else:
        print('islem gecersiz')

def bakiyeSorgulama(hesapBilgisi):
    print(f'{hesapBilgisi['hesapNo']} nolu hesabinizin bakiyesi {hesapBilgisi['bakiye']} turk lirasidir')

paraCek(mehmetHesap,2000)
bakiyeSorgulama(mehmetHesap)