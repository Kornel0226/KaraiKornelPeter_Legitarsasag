from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from LegiTarsasag import LegiTarsasag
from JegyFoglalas import JegyFoglalas
from datetime import datetime

# Előre feltöltött adatok
legi_tarsasag = LegiTarsasag("Pycharm Airlines")

jarat1 = BelfoldiJarat("B101", "Budapest", 10000, legi_tarsasag, datetime(2025, 7, 1, 8, 30))
jarat2 = BelfoldiJarat("B202", "Debrecen", 8000, legi_tarsasag, datetime(2025, 7, 1, 10, 15))
jarat3 = NemzetkoziJarat("N303", "London", 50000, legi_tarsasag, datetime(2025, 7, 2, 6, 45))

legi_tarsasag.jarat_hozzaadas(jarat1)
legi_tarsasag.jarat_hozzaadas(jarat2)
legi_tarsasag.jarat_hozzaadas(jarat3)

foglalasok = [
    JegyFoglalas(jarat1, "Kiss Péter"),
    JegyFoglalas(jarat2, "Nagy Anna"),
    JegyFoglalas(jarat3, "Szabó Bence"),
    JegyFoglalas(jarat1, "Varga Lili"),
    JegyFoglalas(jarat3, "Tóth Gábor"),
    JegyFoglalas(jarat2, "Molnár Dóra")
]

def listaz_foglalasok():
    print("\nAktuális foglalások:")
    if foglalasok:
        for f in foglalasok:
            print(f.info())
    else:
        print("Nincsenek foglalások.")

def jegy_foglalas():
    utas_nev = input("Add meg a neved: ")
    print("Elérhető járatok:")
    for i, jarat in enumerate(legi_tarsasag.jaratok):
        print(f"{i+1}. {jarat.info()}")
    try:
        valasztas = int(input("Válassz járatot (sorszám): "))
        if 1 <= valasztas <= len(legi_tarsasag.jaratok):
            jarat = legi_tarsasag.jaratok[valasztas-1]
            foglalas = JegyFoglalas(jarat, utas_nev)
            foglalasok.append(foglalas)
            print(f"Foglalás sikeres! Ár: {jarat.jegyar} Ft")
        else:
            print("Érvénytelen választás.")
    except ValueError:
        print("Hibás bevitel, számot adj meg!")

def foglalas_lemondas():
    utas_nev = input("Add meg a neved a lemondáshoz: ")
    lemondott = False
    for f in foglalasok:
        if f.utas_nev == utas_nev:
            foglalasok.remove(f)
            print("Foglalás lemondva.")
            lemondott = True
            break
    if not lemondott:
        print("Nem található foglalás ezzel a névvel.")

def main_menu():
    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            jegy_foglalas()
        elif valasztas == "2":
            foglalas_lemondas()
        elif valasztas == "3":
            listaz_foglalasok()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main_menu()