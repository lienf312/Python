from random import*
#Näidis 1
arv=randint(0,10)
print(arv)
if arv>5:
    print("****************")
    print(f"Arv {arv} suurem kui 5")
    print("****************")
if arv>5: print(f"Arv {arv} suurem kui 5")
else:
    print(f"Arv {arv} vähem kui 5")

#Näidis 2
arv=randint(-10,10)
if arv>0:
    print("Positiivne")
else:
    print("Negatiivne")

if arv>0:
    print("Positiivne")
elif arv==0:
    print("0")
else:
    print("Negatiivne")


    #isalnum()	
#isdecimal()	
#isdigit()	
#isidentifier()	
#islower()	
#isnumeric()	
#isprintable()	
#isspace()	
#istitle() 	
#isupper()

nimi = input("Sisesta nimi: ")
if nimi.isupper() and nimi == "JUKU":
   print("Lähme kinos")

vanus=int(input("Kui vana sa oled?"))
if vanus<0 or vanus>100:
     pilet="!!!"
elif vanus<6:
     pilet="Tasuta"
elif vanus<=14:
     pilet="Lastepilet"
elif vanus<=65:
     pilet="Täospilet"
elif vanus<=100:
     pilet="Sooduspilet"


nimi1= input("Sisesta nimi: ")
nimi2= input("Sisesta nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
    print("Te olete pinginaabrid")
if nimi1 == "Nikita" and nimi2 == "jelena" or  nimi1 == "jelena" and nimi2 == "Nikita" :
   
    print("Te olete pinginaabrid")


    









