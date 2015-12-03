from tkinter import *
from tkinter import ttk
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
import os
from itertools import tee

x = symbols('x')


def leia_nullkohad(sisend):
    vastus = []
    nullkohad = solve(sisend, x)
    for i in nullkohad:
        vastus.append((i,0))
    return list(map(str, vastus))


def lahenda_võrrand(sisend):
    return solve(sisend, x)


def leia_miinimum(sisend):
    tuletis = diff(sisend, x)
    if diff(tuletis, x) != 0:
        nullkohad = solve(tuletis)
        minimum = []
        for i in nullkohad:
            if diff(tuletis, x).subs(x, i) > 0:
                minimum.append(i)
        if len(minimum) > 0:
            vastus = []
            for i in minimum:
                vastus.append((i, eval(sisend.replace('x', ('('+str(i)+')')))))
                return list(map(str, vastus))
        else:
            return ['Puudub']
    else:
        return ['Puudub']


def leia_maksimum(sisend):
    tuletis = diff(sisend, x)
    if diff(tuletis, x) != 0:
        nullkohad = solve(tuletis)
        maksimum = []
        for i in nullkohad:
            if diff(tuletis, x).subs(x, i) < 0:
                maksimum.append(i)
        if len(maksimum) > 0:
            vastus = []
            for i in maksimum:
                vastus.append((i, eval(sisend.replace('x', '('+str(i)+')'))))
                return list(map(str, vastus))
        else:
            return ['Puudub']
    else:
        return ['Puudub']


def paarideks(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def leia_kasvamine(sisend):
    if diff(diff(sisend, x), x) != 0:
        vaheldus_piirkond = solve(diff(sisend))
        algne_list = ['-L', 'L']

        for i in range(len(vaheldus_piirkond)):
            algne_list.insert(1, vaheldus_piirkond[i-1])

        intervalid = []
        for paar in paarideks(algne_list):
            intervalid.append(paar)

        kasvab = []
        for i in intervalid:
            if 'L' in i:
                kasvab_parameeter = True
                for arv in range(i[0], 30):
                    if diff(sisend).replace('x', '('+str(arv)+')') < 0:
                        kasvab_parameeter = False
                    else:
                        kasvab_parameeter = True
                if kasvab_parameeter:
                    kasvab.append(i)
            if '-L' in i:
                kasvab_parameeter = True
                for arv in range(-30, i[1]):
                    if diff(sisend).replace('x', '('+str(arv)+')') < 0:
                        kasvab_parameeter = False
                    else:
                        kasvab_parameeter = True
                if kasvab_parameeter:
                    kasvab.append(i)
            if 'L' not in i and '-L'not in i:
                kasvab_parameeter = True
                for arv in range(i[0], i[1]):
                    if diff(sisend).replace('x', '('+str(arv)+')') < 0:
                        kasvab_parameeter = False
                    else:
                        kasvab_parameeter = True
                if kasvab_parameeter:
                    kasvab.append(i)

        return list(map(str, list(kasvab)))
    else:
        return ['Puduub']


def leia_kahanemine(sisend):
    if diff(diff(sisend, x), x) != 0:
        vaheldus_piirkond = solve(diff(sisend))
        algne_list = ['-L', 'L']

        for i in range(len(vaheldus_piirkond)):
            algne_list.insert(1, vaheldus_piirkond[i-1])

        intervalid = []
        for paar in paarideks(algne_list):
            intervalid.append(paar)

        kahaneb = []
        for i in intervalid:
            if 'L' in i:
                kahaneb_parameeter = True
                for arv in range(i[0], 30):
                    if diff(sisend).replace('x', '('+str(arv)+')') > 0:
                        kahaneb_parameeter = False
                    else:
                        kahaneb_parameeter = True
                if kahaneb_parameeter:
                    kahaneb.append(i)
            if '-L' in i:
                kahaneb_parameeter = True
                for arv in range(-30, i[1]):
                    if diff(sisend).replace('x', '('+str(arv)+')') > 0:
                        kahaneb_parameeter = False
                    else:
                        kahaneb_parameeter = True
                if kahaneb_parameeter:
                    kahaneb.append(i)
            if 'L' not in i and '-L'not in i:
                kahaneb_parameeter = True
                for arv in range(i[0], i[1]):
                    if diff(sisend).replace('x', '('+str(arv)+')') > 0:
                        kahaneb_parameeter = False
                    else:
                        kahaneb_parameeter = True
                if kahaneb_parameeter:
                    kahaneb.append(i)
        if len(kahaneb) > 0:
            return list(map(str, list(kahaneb)))
        else:
            return ['Puduub']
    else:
        return ['Puudub']



def lisa_graafik(formula):
    x = np.arange(-10, 10, 0.1)
    y = eval(formula)
    plt.figure(figsize=(5,5))
    plt.ylim(-10, 10)
    plt.plot(x, y)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    init_printing(use_latex= 'mathjax')
    x = symbols('x')
    lateks = latex(eval(formula))
    plt.title('$%s$' %lateks, fontsize = 25)
    plt.savefig('graafik.png')
    img = PhotoImage(file="graafik.png")
    graaf = Label(image=img)
    graaf.image = img
    graaf.pack( side = RIGHT)




def näita_tulemus():
    if valem.get() != '':
        nullkohad_string = ttk.Label(raam, text='Nullkohad_BETA: ', font=('Cambria Math', 10, 'bold'))
        nullkohad_string.place(x=90, y=240)

        nullkohad_vastus = ttk.Label(raam, text=[' , '.join(leia_nullkohad(valem.get()))], font=('Cambria Math', 10, 'bold'))
        nullkohad_vastus.place(x=250, y=240)
        # Tegin ekstreemumite leidmist korda, peaks nüüd korrektselt töötama
        miinimum_string = ttk.Label(raam, text='Miinimum_BETA:', font=('Cambria Math', 10, 'bold'))
        miinimum_string.place(x=90, y=290)

        minimum_vastus = ttk.Label(raam, text=[' , '.join(leia_miinimum(valem.get()))], font=('Cambria Math', 10, 'bold'))
        minimum_vastus.place(x=250, y=290)

        maksimum_string = ttk.Label(raam, text='Maksimum_BETA:', font=('Cambria Math', 10, 'bold'))
        maksimum_string.place(x=90, y=340)

        maksimum_vastus = ttk.Label(raam, text=[' , '.join(leia_maksimum(valem.get()))], font=('Cambria Math', 10, 'bold'))
        maksimum_vastus.place(x=250, y=340)

        # # Töötab hetkel ainult kui on paraboolne funktsioon, kus on ainult 1 vaheldumispunkt (Alpha v0.1)
        kasvab_string = ttk.Label(raam, text='Kasvab_ALPHA:', font=('Cambria Math', 10, 'bold'))
        kasvab_string.place(x=90, y=390)
        #
        kasvab_vastus = ttk.Label(raam, text=[' , '.join(leia_kasvamine(valem.get()))], font=('Cambria Math', 10, 'bold'))
        kasvab_vastus.place(x=250, y=390)
        # # Töötab hetkel ainult kui on paraboolne funktsioon, kus on ainult 1 vaheldumispunkt (Alpha v0.1)
        kahaneb_string = ttk.Label(raam, text='Kahaneb_ALPHA:', font=('Cambria Math', 10, 'bold'))
        kahaneb_string.place(x=90, y=440)
        #
        kahaneb_vastus = ttk.Label(raam, text=[' , '.join(leia_kahanemine(valem.get()))], font=('Cambria Math', 10, 'bold'))
        kahaneb_vastus.place(x=250, y=440)
        #
        # # neid tuleb alles teha (Alpha v0.1)
        # # Mingi hästi väike alpha nendest tehtud, et saavad mõnikord aru, kuid teine tuletis on lihtsalt arv (Alpha v0.1)
        # kumerus_string = ttk.Label(raam, text='Kumerus_ALPHA:', font=('Cambria Math', 10, 'bold'))
        # kumerus_string.place(x=90, y=490)
        #
        # kumerus_vastus = ttk.Label(raam, text=[' , '.join(leia_kumerus(valem.get()))], font=('Cambria Math', 10, 'bold'))
        # kumerus_vastus.place(x=250, y=490)
        #
        # nõgusus_string = ttk.Label(raam, text='Nõgusus:_ALPHA', font=('Cambria Math', 10, 'bold'))
        # nõgusus_string.place(x=90, y=540)
        #
        # nõgusus_vastus = ttk.Label(raam, text=[' , '.join(leia_nõgusus(valem.get()))], font=('Cambria Math', 10, 'bold'))
        # nõgusus_vastus.place(x=250, y=540)
        #
        # # Seda saab varsti juba beta-ks nimetada :D (Alpha v0.1)
        # käänupunkt_string = ttk.Label(raam, text='Käänupunkt_ALPHA:', font=('Cambria Math', 10, 'bold'))
        # käänupunkt_string.place(x=90, y=590)
        #
        # käänupunkt_vastus = ttk.Label(raam, text=leia_käänupunkt(valem.get()), font=('Cambria Math', 10, 'bold'))
        # käänupunkt_vastus.place(x=250, y=590)
        lisa_graafik(valem.get())

    else:
        tühi_sisend = ttk.Label(raam, text='Sisend on tühi.')
        tühi_sisend.place(x=150, y=240)


raam = Tk()
raam.title('PLOTMASTER BASIC ALHPA 0.2.1')
kõrgus = 800
laius = 1300
raam.geometry(str(laius)+'x'+str(kõrgus))


silt = ttk.Label(raam, text='Sisesta oma valem: ',  font=('Cambria Math', 13, 'bold'))
silt.place(x = laius/2.3, y= 0, width = 160, height=60)

valem = ttk.Entry(raam, width=40)
valem.place(x = laius/2.53, y= 70, width = 250, height=60)

arvuta_nupp = ttk.Button(raam, text='Arvuta!', command=näita_tulemus)
arvuta_nupp.place(x=laius/2.25, y=140, width=130, height=40)


def on_closing():
    if os.path.isfile('graafik.png'):
        os.remove('graafik.png')
        sys.exit()
    else:
        sys.exit()

raam.protocol("WM_DELETE_WINDOW", on_closing)
raam.mainloop()
