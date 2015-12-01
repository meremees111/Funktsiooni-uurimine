from tkinter import *
from tkinter import ttk
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
import os

x, y, z, t = symbols('x y z t')


def lahenda_võrrand(sisend):
    return solve(sisend, x)

def võta_tuletis(sisend):
    return diff(sisend, x)

def leia_miinimum(sisend):
    nullkohad = solve(sisend, x)
    tuletis = diff(sisend, x)
    minimum = []
    for i in nullkohad:
        if tuletis.replace(x, i) < 0:
            minimum.append(i)
    return map(str, minimum)

def leia_maksimum(sisend):
    nullkohad = solve(sisend, x)
    tuletis = diff(sisend, x)
    maksimum = []
    for i in nullkohad:
        if tuletis.replace(x, i) > 0:
            maksimum.append(i)
    return map(str, maksimum)

def leia_kasvamine(sisend):
    tuletis = diff(sisend, x)
    i = 0
    if solve(tuletis)[i]+2 > 0 and solve(tuletis)[i]+3 > 0:
        return map(str, [solve(tuletis)[i], 'L'])

def leia_kahanemine(sisend):
    tuletis = diff(sisend, x)
    i = 0
    if solve(tuletis)[i]-2 < 0 and solve(tuletis)[i]-3 < 0:
        return map(str, ['-L', solve(tuletis)[i]])

def leia_käänupunkt(sisend):
    if len(solve(diff(diff(sisend)))) == 0:
        return ['Puduub']
    else:
        return solve(diff(diff(sisend)))

def leia_kumerus(sisend):
    teine_tuletis = diff(diff(sisend))
    try:
        if teine_tuletis < 0:
            return ['-L', 'L']
        else:
            return ['Puduub']
    except:
        return 'See meetod pole veel lisatud'

def leia_nõgusus(sisend):
    teine_tuletis = diff(diff(sisend))
    try:
        if teine_tuletis > 0:
            return ['-L', 'L']
        else:
            return 'Puudub'
    except:
        return 'See meetod pole veel lisatud'


def lisa_graafik(formula, xkohad):
    x = np.array(xkohad)
    y = eval(formula)
    plt.plot(x, y)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.savefig('graafik.png')
    tahvel = Canvas(raam, height=600, width=800, background='white')
    img = PhotoImage(file="graafik.png")
    graaf = Label(image=img)
    graaf.image = img
    graaf.pack( side = RIGHT)



def näita_tulemus():
    if valem.get() != '':
            nullkohad_string = ttk.Label(raam, text='Nullkohad_BETA: ', font=('Cambria Math', 10, 'bold'))
            nullkohad_string.place(x=90, y=240)

            nullkohad_vastus = ttk.Label(raam, text=[' , '.join(lahenda_võrrand(valem.get()))], font=('Cambria Math', 10, 'bold'))
            nullkohad_vastus.place(x=250, y=240)

            miinimum_string = ttk.Label(raam, text='Miinimum_BETA:', font=('Cambria Math', 10, 'bold'))
            miinimum_string.place(x=90, y=290)

            minimum_vastus = ttk.Label(raam, text=[' , '.join(leia_miinimum(valem.get()))], font=('Cambria Math', 10, 'bold'))
            minimum_vastus.place(x=250, y=290)

            maksimum_string = ttk.Label(raam, text='Maksimum_BETA:', font=('Cambria Math', 10, 'bold'))
            maksimum_string.place(x=90, y=340)

            maksimum_vastus = ttk.Label(raam, text=[' , '.join(leia_maksimum(valem.get()))], font=('Cambria Math', 10, 'bold'))
            maksimum_vastus.place(x=250, y=340)

            # Töötab hetkel ainult kui on paraboolne funktsioon, kus on ainult 1 vaheldumispunkt (Alpha v0.1)
            kasvab_string = ttk.Label(raam, text='Kasvab_ALPHA:', font=('Cambria Math', 10, 'bold'))
            kasvab_string.place(x=90, y=390)

            kasvab_vastus = ttk.Label(raam, text=[' , '.join(leia_kasvamine(valem.get()))], font=('Cambria Math', 10, 'bold'))
            kasvab_vastus.place(x=250, y=390)
            # Töötab hetkel ainult kui on paraboolne funktsioon, kus on ainult 1 vaheldumispunkt (Alpha v0.1)
            kahaneb_string = ttk.Label(raam, text='Kahaneb_ALPHA:', font=('Cambria Math', 10, 'bold'))
            kahaneb_string.place(x=90, y=440)

            kahaneb_vastus = ttk.Label(raam, text=[' , '.join(leia_kahanemine(valem.get()))], font=('Cambria Math', 10, 'bold'))
            kahaneb_vastus.place(x=250, y=440)

            # neid tuleb alles teha (Alpha v0.1)
            # Mingi hästi väike alpha nendest tehtud, et saavad mõnikord aru, kuid teine tuletis on lihtsalt arv (Alpha v0.1)
            kumerus_string = ttk.Label(raam, text='Kumerus_ALPHA:', font=('Cambria Math', 10, 'bold'))
            kumerus_string.place(x=90, y=490)

            kumerus_vastus = ttk.Label(raam, text=[' , '.join(leia_kumerus(valem.get()))], font=('Cambria Math', 10, 'bold'))
            kumerus_vastus.place(x=250, y=490)

            nõgusus_string = ttk.Label(raam, text='Nõgusus:_ALPHA', font=('Cambria Math', 10, 'bold'))
            nõgusus_string.place(x=90, y=540)

            nõgusus_vastus = ttk.Label(raam, text=[' , '.join(leia_nõgusus(valem.get()))], font=('Cambria Math', 10, 'bold'))
            nõgusus_vastus.place(x=250, y=540)

            # Seda saab varsti juba beta-ks nimetada :D (Alpha v0.1)
            käänupunkt_string = ttk.Label(raam, text='Käänupunkt_ALPHA:', font=('Cambria Math', 10, 'bold'))
            käänupunkt_string.place(x=90, y=590)

            käänupunkt_vastus = ttk.Label(raam, text=leia_käänupunkt(valem.get()), font=('Cambria Math', 10, 'bold'))
            käänupunkt_vastus.place(x=250, y=590)

            näita_graafik = ttk.Button(raam, text='Näita graafik!')
            näita_graafik.place(x=125, y=650, height=60, width=140)

    else:
        tühi_sisend = ttk.Label(raam, text='Sisend on tühi.')
        tühi_sisend.place(x=150, y=240)


raam = Tk()
raam.title('Funktsiooni uurija v.0.1 ALPHA')
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

raam.protocol("WM_DELETE_WINDOW", on_closing)
raam.mainloop()
