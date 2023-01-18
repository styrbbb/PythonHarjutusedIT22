#Thorian Perk
#10.01.2023
#GP, ülesanne5
import tkinter
import tkinter.messagebox

def arvuta():
      hind=float(sisestus.get())
      km=float(var.get())
      m=hind*km/100
      k.config(text=m)
      h=hind+m
      t.config(text=h)

from tkinter import *

aken = Tk()
aken.resizable(0, 0)
aken.iconbitmap('favicon.ico')
aken.title('Käibemaksukalkulaator')
aken.geometry("300x300")

#Käibemaksu sisestus
tekst = Label(aken,
                      text="Hind käibemaksuta: ",
                      font="Tahoma 12",
                      padx=2,
                      pady=2)
tekst.grid(row=0, column=0, sticky="w")
#Sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0, column=1, sticky="w")


#Käibemaksu valikud
tekst = Label(aken,
                      text="Käibemaksumäär",
                      font="Tahoma 12",
                      padx=2,
                      pady=2)
tekst.grid(row=1, column=0, sticky="w")

#radio
#valikud
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value =9)
valikukast.grid(row=1, column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20)
valikukast.grid(row=2, column=1)

tekst = Label(aken,
                      text="_______________________________________",
                      font="Tahoma 8",
                      padx=2,
                      pady=2)
tekst.grid(row=3, column=0, columnspan=2)

#Km
tekst = Label(aken,
                      text="Käibemaks: ",
                      font="Tahoma 12",
                      padx=2,
                      pady=2)
tekst.grid(row=4, column=0, sticky="w")

k = Label(aken,
                    text="0.00€",
                    font="Tahoma 12",
                    padx=2,
                    pady=2)
k.grid(row=4, column=1, sticky="w")

#Summa või hind, jne
tekst = Label(aken,
                      text="Hind käibemaksuga: ",
                      font="Tahoma 12",
                      padx=2,
                      pady=2)
tekst.grid(row=6, column=0, sticky="w")

t = Label(aken,
                      text="0.00€",
                      font="Tahoma 12",
                      padx=2,
                      pady=2)
t.grid(row=6, column=1, sticky="w")

#Vaherida
tekst = Label(aken,
                      text="")
tekst.grid(row=7, column=0, sticky="w")

#nupud
nupp1 = Button(aken, text="OK", width=10, command=arvuta)
nupp1.grid(row=8, column=1)








"""
tekst = Label(aken,
                      text="Siia tuleb vastus!",
                      font="Tahoma 12",
                      padx=20,
                      pady=20)
tekst.grid(row=0, column=0, columnspan=4)

#Nupud 1 rida
nupp1 = Button(aken, text="7", width=4, font="Tahoma 12")
nupp1.grid(row=1, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="8", width=4, font="Tahoma 12")
nupp2.grid(row=1, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="9", width=4, font="Tahoma 12")
nupp3.grid(row=1, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="/", width=4, font="Tahoma 12")
nupp4.grid(row=1, column=3, padx=2, pady=2)

#Nupud 2 rida
nupp1 = Button(aken, text="4", width=4, font="Tahoma 12")
nupp1.grid(row=2, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="5", width=4, font="Tahoma 12")
nupp2.grid(row=2, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="6", width=4, font="Tahoma 12")
nupp3.grid(row=2, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="*", width=4, font="Tahoma 12")
nupp4.grid(row=2, column=3, padx=2, pady=2)

#Nupud 3 rida
nupp1 = Button(aken, text="1", width=4, font="Tahoma 12")
nupp1.grid(row=3, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="2", width=4, font="Tahoma 12")
nupp2.grid(row=3, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="3", width=4, font="Tahoma 12")
nupp3.grid(row=3, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="-", width=4, font="Tahoma 12")
nupp4.grid(row=3, column=3, padx=2, pady=2)

#Nupud 4 rida
nupp1 = Button(aken, text=",", width=4, font="Tahoma 12")
nupp1.grid(row=4, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="0", width=4, font="Tahoma 12")
nupp2.grid(row=4, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="=", width=4, font="Tahoma 12")
nupp3.grid(row=4, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="+", width=4, font="Tahoma 12")
nupp4.grid(row=4, column=3, padx=2, pady=2)

"""

aken.mainloop()