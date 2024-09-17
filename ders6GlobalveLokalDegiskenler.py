x='global x' #global degisken

def fonksiyon(): #fonksiyon ici degiskenler fonksiyon disini etkilemez.
    x='lokal x' #lokal degisken
    print(x)
fonksiyon()
print(x)

a=50
def test():
    global a #global degiskeni ifadesi gelince a=50 degil a=100 oldu.
    print(f'x {a}')
    a=100
    print(f'x degistirildi: {a}')

test()
print(a)