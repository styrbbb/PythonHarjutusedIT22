#Thorian Perk
#11.01.2023
#GP, ülesanne6



from tkinter import *

#akna seaded
aken = Tk()
aken.title('Joonistamine')
#aken.iconbitmap('favicon.ico')

#lõuendi loomine
louend = Canvas(aken, width=500, height=300)
louend.pack()

#kujundite loomine
louend.create_rectangle(0, 0, 500, 150, fill="white", width=0)
louend.create_rectangle(0, 150, 500, 300, fill="red", width=0)
louend.create_polygon(0, 0, 250, 150, 0, 300, fill="blue", width=0)

aken.mainloop()