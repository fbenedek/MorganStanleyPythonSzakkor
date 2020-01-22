### Python 3 puska - "cheat sheet" ###
# 
## Változók, alapműveletek ##
# a számítógépben az adatokat "változókban" tároljuk 
valtozoSzam = 7 # számot is tárolhatok
valtozoSzoveg = "Hajdiho" #szöveget is ("string")
valtozoLogikai = True #igaz-hamis értékeket is (True, False)

## műveletek számokkal ##
# számok típusa: int (egész), float (tizedes tört (a "float" a "lebegőpontosból" jön))
eredmeny = ((valtozoSzam + 10)/3*2)**(2)%2 #+,-,*,/, zárójelek működnek, ** hatványozás, a%b a maradéka b-vel osztva
strszam = "7"
szam = int(strszam) #betű átalakítása egész számmá
strSzam = "7.05"
szam = float(strSzam) #string átalakítás törtté
szoveg = str(szam) #szám átalakítása szöveggé


# kinyomtatás a képernyőre #
print(eredmeny) #számot, vagy bármilyen típusú változót is kiprintelhetek így
print('Az eredmény: '+ str(eredmeny))

# műveletek stringekkel #
betu = valtozoSzoveg[2] #harmadik betű kiválasztása (0-tól indul a számozás)
resz = valtozoSzoveg[2:] # harmadik betűtől
resz2 = valtozoSzoveg[:5] #hatodik betűig
elsoresz = "Stringeket "
masodikresz = "össze lehet adni!"
szoveg = elsoresz + masodikresz #konkatenálás, vagy egymás után fűzés
print(szoveg)
if 'ö' in szoveg: #van-e benne 'ö'-vel egyenlő részlet?
    print("Nem Szegedi vagy véletlen?")
    

# logikai értékek használata: elágazás #
if valtozoLogikai:
    print("Igaz!")
    
# egyenlőség eldöntése:
if 2 == 3:
    print("Valami gond van!")
elif 3 != 3: #if után egy másik leágazás - =! a "nemegyenlő"
    print("Még mindig nem jó!")
else:
    print("Minden OK")
    
## ciklusok ##
    
# while: addig csinálok valamit, amíg a while után írt feltétel igaz. Ha egyszer hamis, abbahagyom
    
a = 4
while a>-1: # amíg a -1-nél nagyobb
    print(a) # kinyomtatom a-t. behúzás mutatja, hogy hol a van ciklus "hasa"!
    a = a -1 # a értékét 1-el csökkentem
print("Ezt csak egyszer írom ki")
    
#for: VÉGIGMEGYEK valamin. ez lehet egy számsor:
for szam in range(0,36,6): #range(mettől, meddig,hanyasával) létrehoz egy számsorozatot. Ezen ugrál végig a for.
    print(szam)
    
#lehet mondjuk betűk sorozata is, mint egy string:
for betu in "betusorozat":
    print(betu)

## függvények ##

def osszeado(szam1, szam2): # def Függvény neve(bemenetek):
    osszeg = szam1 + szam2 #amíg a behűzás tart, az a rész a fg-hez tartozik
    return osszeg # nem kötelező returnolni.

osszeg = osszeado(10,12)
print(osszeg)

## könyvtárhasználat ##

import time #innentől a "time" könyvtár függvényeit használhatom olyan alakban, hogy time.fgnev
import datetime as dt #innentől a "datetime" könyvtár függvényeit használhatom olyan alakban, hogy dt.fgnev

jelenlegiIdo = time.time() #egy adott időponttól ("epoch") eltelt mp-ek floatban
time.sleep(3) # 3 másodpercet várokozhat így a program.
varkozashossza = time.time() - jelenlegiIdo # így lehet stoppert "építeni"!


## fájlkezelés ##
#olvasás#
with open("fajlom.txt", 'r') as olvasnivalo:
    #egeszfajl = fajlom.read() - így is lehet, de inkább soronként!
    for sor in olvasnivalo:
        print(sor) #beolvasom és kinyomtatom a tartalmát.
        #ide írhatok bármit, amit művelni akarok a sorral.
#írás#
with open("fajlom2.txt", 'w') as irnivalo:
    irnivalo.write('Hahó!\n') #egy sorba beleírtam, és a végére tettem egy sortörést.
    #hogyha egyszerre sok sort akarok írni, akkor listát is használhatok:
    soksorom = ["egy\n", "kettő\n", "spam\n"]  #sortörés kell!
    irnivalo.writelines(soksorom)
#ha így írom a fájlt, akkor mindig kitörlöm a tartalmát megnyitáskor, és a 'nulláról' kezdem.
#hozzáfűzés, 'append'#
with open("fajlom2.txt", 'a') as nembantomdeirom:
    nembatomdeirom.write('Sor!\n')
    #most a "Sor!" nem a fájl első sorába került a többi törlésével, hanem az eddigi utolsó után


 

