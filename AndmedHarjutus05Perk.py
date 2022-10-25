#Thorian Perk
#25.10.22
#harjutus05

#Õpilaste nimede muutmine
jrk  = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
opilased.remove("Mario")
opilased.insert(3, "Kario")
for i in opilased:
    print(f"{jrk}.{i}")
    jrk+=1

print("-----------------------")
#Nimede lisamine loendisse
nimed = []
for i in range(5):
    nimi = input("Lisa nimi loendisse: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
print(f"Viimati lisatud nimi: {nimed[-1]}")