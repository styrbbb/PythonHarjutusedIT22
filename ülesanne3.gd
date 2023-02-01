extends Node


#Thorian Perk
#Ülesanne3
#01.02.2023

func _ready():
	
	print("-----ÜLESANNE 5-----")
	
	tootasu(41,10)
	
	
	
func tootasu(h,t):
	var tasu
	if h <= 40:
		tasu = h*t
	else:
		tasu = 40*t+(h-40)*1.5*t
	print(tasu)
