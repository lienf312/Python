p = [] 
i = [] 

def Lisa_andmed(p: list, i: list):
    """
    """
    nimi = input("Sisesta nimi: ")
    while not nimi.isalpha():
        print("Nimi peab koosnema ainult tähtedest.")
        nimi = input("Sisesta nimi: ")

    while True:
        try:
            palk = float(input("Sisesta palk: "))
            break
        except ValueError:
            print("Palk peab olema arv. Proovi uuesti.")
    p.append(palk)
    i.append(nimi)
    print(f"Andmed {nimi} ja palgaga {palk} on lisatud.")

def Kustuta_andmed(p: list, i: list):
    """
    """
    nimi = input("Sisesta kustutamiseks nimi: ")
    if nimi in i:
        index = i.index(nimi) 
        i.pop(index) 
        p.pop(index)  
        print(f"Andmed {nimi} on kustutatud.")
    else:
        print(f"Nimi {nimi} ei leitud.")

def Suurim_palk(p: list, i: list):
    """
    """
    if len(p) == 0:
        print("Loend on tühi!")
        return

    suurim = max(p) 
    index = p.index(suurim) 
    print(f"Inimene kõige suurema palgaga: {i[index]} ja palk {suurim}")

def Sorteerimine(p: list, i: list):
    """
    """
    v=input("Vali märk: > (kasvav) või < (kahanev)")
    #Tryexcept koos while True'ga
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])): #p[n]
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    
    print("Loendid on sorteeritud!")

def Vordsed_palgad(p: list, i: list):
    """
    """
    if len(p) == 0:
        print("Loend on tühi!")
        return

    hulk = set(p)
    for palk in hulk:
        if p.count(palk) > 1:
            print(f"Palk {palk} on järgmistele inimestele:")
            for index, value in enumerate(p):
                if value == palk:
                    print(f"{i[index]}")


def Sorteeri_nimi_jargi(i: list, p: list):
    """
    """
    suund = input("Vali suund: A-Z või Z-A: ").strip().upper()
    if suund not in ["A-Z", "Z-A"]:
        print("Vale valik!")
        return

    kasvav = suund == "A-Z"
    for n in range(len(i)):
        for m in range(n + 1, len(i)):
            if (kasvav and i[n] > i[m]) or (not kasvav and i[n] < i[m]):
                i[n], i[m] = i[m], i[n]
                p[n], p[m] = p[m], p[n]
                print("Nimed on sorteeritud!")


def Kustuta_alla_keskmise(p: list, i: list):
    """
    """
    if len(p) == 0:
        print("Loend on tühi!")
        return
    keskmine = sum(p) / len(p)
    print(f"Keskmine palk on: {keskmine}")
    indeksid = [index for index, palk in enumerate(p) if palk < keskmine]

for index in reversed(indeksid): # удаляем с конца, чтобы индексы не сбились
    print(f"Kustutatud: {i[index]} palgaga {p[index]}")
    p.pop(index)
    i.pop(index)


def Vorminda_andmed(p: list, i: list):
    """
    """
    for j in range(len(i)):
        i[j] = i[j].capitalize()
        p[j] = int(p[j])
    print("Andmed on vormindatud!")


def Tuleviku_palk(p: list, i: list):
    """
    """
    nimi = input("Sisesta töötaja nimi: ").capitalize()
    if nimi in i:
        index = i.index(nimi)
        try:
            t = int(input("Mitu aastat? "))
            tuleviku_palk = p[index] * (1.05 ** t)
            print(f"{nimi} palk {t} aasta pärast on {round(tuleviku_palk, 2)}")
        except ValueError:
            print("Aastad peavad olema arv.")
    else:
        print("Töötajat ei leitud.")

