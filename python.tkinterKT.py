#Python.tkinter KT
#Thorian Perk
#17.01.2023

def mahlapakkide_arv():
         oun=float(sisestus.get())
         m = round(oun*0.4/3)
         print(m)
         k.config(text=m)
        
        
from tkinter import *

#ül. 4.2 Õunamahla tegemine + tkinter

#Akna seaded
aken = Tk()
aken.title('Õunamahla tegemine KT')
aken.geometry("310x250")

#aken.iconbitmap('favicon.ico')

#Vaherida
tekst = Label(aken,
                      text="")
tekst.grid(row=0, column=0, sticky="w")

#Õunte koguse sisestus
tekst = Label(aken,
                      text="Õunte kogus kg: ",
                      font="Tahoma 12",
                      padx=2,
                      pady=2)
tekst.grid(row=1, column=0, sticky="w")
#Sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=1, column=1, sticky="w")

#-
tekst = Label(aken,
                      text="___________________________________________",
                      font="Tahoma 8",
                      padx=2,
                      pady=2)
tekst.grid(row=2, column=0, columnspan=2)


#Vaherida
tekst = Label(aken,
                      text="")
tekst.grid(row=3, column=0, sticky="w")

#k
tekst = Label(aken,
                      text="Mahlapakkide arv: ",
                      font="Tahoma 12",
                      padx=2,
                      pady=2)
tekst.grid(row=4, column=0, sticky="w")

k = Label(aken,
                    text="0",
                    font="Tahoma 12",
                    padx=2,
                    pady=2)
k.grid(row=4, column=1, sticky="w")

#Vaherida
tekst = Label(aken,
                      text="")
tekst.grid(row=5, column=0, sticky="w")

#Kalkulaatori nupp
nupp1 = Button(aken, text="OK", width=10, command=mahlapakkide_arv)
nupp1.grid(row=6, column=1)






 
#oun = int(input("Õunte kogus kilogrammides:  "))
#print(mahlapakkide_arv(oun))


