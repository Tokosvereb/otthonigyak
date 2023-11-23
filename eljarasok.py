import random
import math

"""Kérj be 1 páros számot a felhasználótól. (1 pont)
Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)"""

def elsofeladat():
    szam = int(input("Kérlek, adj meg egy páros számot: "))
    
    while szam % 2 != 0:
        print("nem páros")
        szam =int(input("Adj meg egy páros számot:"))
        if szam % 2 == 0:
            print("Helyes")



"""Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. 
Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!”"""

def masodikfeladat():
    i = 0
    szamlalo = 0

    while i < 13:
        szam = math.floor(random.random() * 149 + 10)
        
        if szam % 3 == 0:
            szamlalo += 1

        i += 1

    print(f"A számok között {szamlalo} db 3-mal osztható szám van")
    return szamlalo
        
         #nemvágom hogya gecibe kene azt megoldani hogy kiirja hogy hany db 3al oszthato szam van

"""Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot. 
 Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”
Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor! 
"""

def harmadikfeladat(szoveg:str,szam:int):
    hossz=len(szoveg)
    if hossz < szam:
        print("Nincs N karakter!")
    
    else:
        print(szoveg.upper()[szam-1]*3)  #ez nagyjabol vilagos de gyakorolni kell

"""Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.
Hány nevet adott meg a felhasználó? 
A kiírás formája: „A felhasználó 12 nevet adott meg.”
"""

def negyedikfeladat():
    szamlalo = 0
    nev = str(input("Adj meg egy nevet:"))
    
    while nev !="@":
        nev = str(input("Adj meg egy nevet:"))
        szamlalo += 1

    print(f"A felhasználó {szamlalo} nevet adott meg")

"""Szimuláljuk a kő-papír-olló játékot. 
Írj eljárást, amiben: 
A felhasználótól bekérjük a tippjét, ami kő/papír/olló lehet. Alakítsd át csupa kisbetűssé a szöveget, majd tárold el a felhasznalo_tippje változóban. 
Ezután a gép generál egy egész számot [1,3] között.  1 kő, 2 papír  3 olló. Tárold el a gep_tippje változóban
Ezután írd ki, hogy ki nyert!
	Ha a két szó ugyanaz, írja ki, hogy Döntetlen. 
	Egyéb esetben azt írja ki, aki győzött!
++ Ha valami más szót ad meg a felhasznló  a kő, papír, ollón kívül, akkor kérje be újra!"""


def otodikfeladat():
    while True:
        felhasznalo_tippje = input("Válassz kő, papír vagy olló közül: ").lower()

        if felhasznalo_tippje not in ['kő', 'papír', 'olló']:
            print("Csak kő, papír vagy olló megadása lehetséges. Kérlek, próbáld újra.")
            continue

        gep_tippje = random.randint(1, 3)
        if gep_tippje == 1:
            gep_tippje = 'kő'
        elif gep_tippje == 2:
            gep_tippje = 'papír'
        else:
            gep_tippje = 'olló'

        print(f"A gép választása: {gep_tippje}")

        if felhasznalo_tippje == gep_tippje:
            print("Döntetlen!")
        elif (felhasznalo_tippje == 'kő' and gep_tippje == 'olló') or \
             (felhasznalo_tippje == 'papír' and gep_tippje == 'kő') or \
             (felhasznalo_tippje == 'olló' and gep_tippje == 'papír'):
            print("Gratulálok, nyertél!")
        else:
            print("Sajnálom, vesztettél!")

        ujra_jatszani = input("Szeretnél újra játszani? (igen/nem): ").lower()
        if ujra_jatszani != 'igen':
            break

