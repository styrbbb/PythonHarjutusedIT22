extends Node


#Thorian Perk
#Ülesanne2
#01.02.2023

var random = RandomNumberGenerator.new()

func _ready():
	print("-----ÜLESANNE 2-----")
	var raha = 80
	var telefon = 60
	
	
	if raha>=telefon:
		print("Saab osta")
	else:
		print("Ei saa osta")



	print("-----ÜLESANNE 3-----")
#mängija elupunktid
	var hp_player = 100 # < sina
#vaenlase elupunktid, NPC (ehk Mitte mängitav character)
	var hp_enemy = 100 
	
	while hp_enemy > 0:
		random.randomize()
		var dmg = random.randi_range(8, 15)
		hp_enemy -= dmg
		print("Life: ", hp_enemy, " ", "Hit: ", dmg)



	print("-----ÜLESANNE 4.1-----")
	
	
	var names = ["Feake","Bradwell","Dreger","Bloggett","Lambole","Daish","Lippiett","Blackie","Stollenbeck",
	"Houseago","Dugall","Sprowson","Kitley","Mcenamin","Allchin","Doghartie","Brierly","Pirrone",
	"Fairnie","Seal","Scoffins","Galer","Matevosian","DeBlase","Cubbin","Izzett","Ebi","Clohisey",
	"Prater","Probart","Samwaye","Concannon","MacLure","Eliet","Kundt","Reyes"]
	
	var biggest = names.max()
	
	names.sort()
	names.append("Thorian")
	names.erase("Reyes")
	
	for name in names:
		print(name)
	print("Suurim väärtus: ",biggest)



	print("-----ÜLESANNE 4.2-----")
	
	var player = {"name":"john", "posx":9, "posy":18, "health":"100", "items":"tool","gold":2}
	var gold = 2
	var max_gold = 60
	
	while max_gold > 0:
		random.randomize()
		var mining = random.randi_range(3, 5)
		max_gold -= mining
		print("Kulda on järel: ", max_gold, " ", "Kulda kaevandatakse: ", mining)
	
	
	
	
	
	
	
	
	
