from tkinter import *
from tkinter import ttk
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
import os

x, y, z, t = symbols('x y z t')
f, g, h = symbols('f g h', cls=Function)


def lahenda_võrrand(sisend):
    return solve(sisend, x)

def võta_tuletis(sisend):
    return diff(sisend, x)

def lisa_graafik(formula, xkohad):
    x = np.array(xkohad)
    y = eval(formula)
    plt.plot(x, y)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    init_printing(use_latex= 'mathjax')
    x = symbols('x')
    lateks = latex(eval(formula))
    plt.title('$%s$' %lateks, fontsize = 25)
    plt.savefig('graafik.png')
    tahvel = Canvas(raam, height=600, width=800, background='white')
    img = PhotoImage(file="graafik.png")
    graaf = Label(image=img)
    graaf.image = img
    graaf.pack( side = RIGHT)



def näita_tulemus():
    if valem.get() != '':
        nullkohad_string = ttk.Label(raam, text='Nullkohad: ', font=('Cambria Math', 10, 'bold'))
        nullkohad_string.place(x=90, y=240)

        nullkohad_vastus = ttk.Label(raam, text=[lahenda_võrrand(valem.get())], font=('Cambria Math', 10, 'bold'))
        nullkohad_vastus.place(x=250, y=240)

        kahaneb_string = ttk.Label(raam, text='Kahaneb:', font=('Cambria Math', 10, 'bold'))
        kahaneb_string.place(x=90, y=290)

        kumerus_string = ttk.Label(raam, text='Kumerus:', font=('Cambria Math', 10, 'bold'))
        kumerus_string.place(x=90, y=340)

        nõgusus_string = ttk.Label(raam, text='Nõgusus:', font=('Cambria Math', 10, 'bold'))
        nõgusus_string.place(x=90, y=390)

        lisa_graafik(valem.get(), range(-10, 10))



    else:
        tühi_sisend = ttk.Label(raam, text='Sisend on tühi.')
        tühi_sisend.place(x=150, y=240)


raam = Tk()
raam.title('PLACEHOLDER')
raam.geometry('1300x800')

silt = ttk.Label(raam, text='Sisesta oma valem: ',  font=('Cambria Math', 13, 'bold'))
silt.place(x = 125, y= 20, width = 160, height=60)

valem = ttk.Entry(raam, width=40)
valem.place(x = 80, y= 100, width = 250, height=60)



arvuta_nupp = ttk.Button(raam, text='Arvuta!', command=näita_tulemus)
arvuta_nupp.place(x=125, y=180, width=160, height=60)

def on_closing():
    if messagebox.askokcancel("Quit", "Kindel, et soovid lõpetada?"):
        os.remove('graafik.png')
        raam.destroy()

#raam.protocol("WM_DELETE_WINDOW", on_closing)
raam.mainloop()
