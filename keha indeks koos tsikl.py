print("Tere! Olen sinu uus sober - Python")
nimi=input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi! ")
while 1:
    try:
        soov=int(input(f"{nimi}!Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
        if soov==1:
            print("Indeksi leidmine")
            while true:
                try:
                    pikkus=int(input("Mis on sinu pikkus?"))

                except:
                        mass=float(input("Mis on sinu kaal?"))
                        indeks=maas/(0.1*pikkus)**2
                        print(nimi,"! Sinu keha indeks on:" ,indeks)
                        break
                
                if indeks < 16:
                      print("Tervisele ohtlik alakaal")
                elif indeks == 16 - 19:
                      print("Alakaal")
                elif indeks == 19 - 25:
                      print("Normaalkaal")
                elif indeks == 25 - 30:
                      print("Ülekaal")
                elif indeks == 30 - 35:
                      print("Rasvumine")
                elif indeks == 35 - 40:
                      print("Tugev rasvumine")
                elif indeks > 40:
                      print("Tervisele ohtlik rasvumine")

       except:
                 print("Vale kaalu formaat!")
       except:
                 print("Vale pikkuse formaat!")
  
                elif soov==0:
                 print("Kahju! See on väga kasulik info!")
            break 
                else:
                 print("Vale valik. Saab valida ainult 1 voi 0")
       except:
                 print("Vale soov")
