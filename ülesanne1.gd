extends Node


#Thorian Perk
#Ülesanne1
#25.01.2023

var random = RandomNumberGenerator.new()
"""
func _ready():
	print("-----ÜLESANNE 1-----")
	var name = "Thorian"
	var life = 3
	random.randomize()
	var random_number = random.randi_range(0, 19)
	print(name)
	print(life)
	print("Nime pikkus: ", len(name))
	print("Elud +2: ",life + 2)
	print("Suvaline arv 0-19: ",random_number)
"""
