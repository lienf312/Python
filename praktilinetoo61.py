import random

sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

# tõlge eesti > vene
def tolgi_est_ven(sona):
    if sona in sonastik:
        print("Tõlge vene keelde:", sonastik[sona])
    else:
        print("Sõna ei leitud")

# tõlge vene > eesti
def tolgi_ven_est(sona):
    for est, ven in sonastik.items():
        if ven == sona:
            print("Tõlge eesti keelde:", est)
            return
    print("Sõna ei leitud")

# lisa uus sõna
def lisa_sona():
    est = input("Sisesta sõna eesti keeles: ")
    ven = input("Sisesta sõna vene keeles: ")
    sonastik[est] = ven
    print("Sõna lisatud!")

# paranda sõna
def paranda_sona():
    vana = input("Sisesta sõna, mida soovid parandada: ")
    if vana in sonastik:
        uus = input("Sisesta uus sõna: ")
        tolge = sonastik[vana]
        del sonastik[vana]
        sonastik[uus] = tolge
        print("Sõna parandatud!")
    else:
        # kontrollime 
        for est, ven in sonastik.items():
            if ven == vana:
                uus = input("Sisesta uus sõna: ")
                sonastik[est] = uus
                print("Sõna parandatud!")
                return
        print("Sõna ei leitud")

# tesе
def teadmiste_test():
    oige = 0
    kokku = 0
    print("Teadmiste test algab!")
    for est, ven in random.sample(list(sonastik.items()), len(sonastik)):
        vastus = input(f"Tõlgi sõna «{est}»: ")
        if vastus.lower() == ven.lower():
            print("Õige!")
            oige += 1
        else:
            print("Vale. Õige vastus oli:", ven)
        kokku += 1
    protsent = (oige / kokku) * 100
    print("Test lõppenud! Sinu tulemus:", int(protsent), "%")

# põhiprogramm
def peamenyy():
    print("Tere tulemast eesti-vene sõnaraamatusse!")
    while True:
        print("\nValikud:")
        print("1 - Tõlge eesti -> vene")
        print("2 - Tõlge vene -> eesti")
        print("3 - Lisa uus sõna")
        print("4 - Paranda sõna")
        print("5 - Teadmiste test")
        print("6 - Välju")
        valik = input("Tee oma valik: ")

        if valik == "1":
            sona = input("Sisesta sõna eesti keeles: ")
            tolgi_est_ven(sona)
        elif valik == "2":
            sona = input("Sisesta sõna vene keeles: ")
            tolgi_ven_est(sona)
        elif valik == "3":
            lisa_sona()
        elif valik == "4":
            paranda_sona()
        elif valik == "5":
            teadmiste_test()
        elif valik == "6":
            print("Head aega!")
            break
        else:
            print("Vale valik")

peamenyy()
