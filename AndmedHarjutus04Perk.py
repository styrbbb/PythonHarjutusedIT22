#Thorian Perk
#19.10.22
#harjutus04
import random


#korrutustabel





#paaris ja paaritu
for i in range(1,12):
if i % 2 = 0:
    print("paaris {i}")
else:
    print("paaritu {i}")


#pank
konto = 10000
intress = 0.05
periood = 5

for i in range(1,periood+1):
    print(f"{i} {round(konto,2)} {round(konto*intress,2)} {round(konto+konto*intress,2)}")
    konto = konto+konto*intress
print(f"Konto seis: {round(konto,2)}")
print(f"Kasum: {round(konto-10000,2)}")


#arvamismäng

loop = 1
while loop==1
    suvarv = random.randint(1,10)
    print(suvarv)
    for i in range(3):
        valik = int(input("Vali arv 1-10: "))
        if valik == suvarv:
            print("WINNER!")
            skoor+=1
            break
        else:
            print("LOSER!")
    loop = int(input("Veel (1/0)? "))
print("GAME OVER")
print(f"Skoor {skoor}")
        
"""
#loto
for i in range (5):
    suv = random.randint(0,9)
    print (suv, end="")


#tärnid
arv = 5
for i in range(5):
    print ("* " * arv)
    #arv = arv + 1
    arv -= 1


arv = 1
for i in range(5):
    print ("* " * arv)
    #arv = arv + 1
    arv += 1


nr = 5
for i in range(nr):
    print("* " * nr)


#jalka
vanus = 16
sugu = "m"

if vanus>=16 and vanus<=18 and sugu=="m":
    print("sobib meeskonda")
else:
    print ("ei sobi")
    

#myyk
hind = 20
if hind<=10:
    ale = 0.1
else:
    ale = 0.2
summa = hind-hind*ale

print(f"Summa: {summa}€")

"""

        
    