from tkinter import *
from tkinter import ttk
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
import os
from itertools import tee
import itertools
import math

x = symbols('x')


def leia_nullkohad(sisend):
    vastus = []
    nullkohad = solve(sisend, x)
    for i in nullkohad:
        if 'I' not in str(i):
            vastus.append((i, 0))
    if len(vastus) > 0:
        return list(map(str, vastus))
    else:
        return ['Puudub']


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


def paarideks(järjend):
    a, b = tee(järjend)
    next(b, None)
    return zip(a, b)


def leia_kasvamine(sisend):
    if diff(diff(sisend, x), x) != 0:
        vaheldus_piirkond = solve(diff(sisend))
        algne_list = ['-\infty', '\infty']

        for i in range(len(vaheldus_piirkond)):
            algne_list.insert(1, vaheldus_piirkond[i-1])

        intervalid = []
        for paar in paarideks(algne_list):
            intervalid.append(paar)

        kasvab = []
        for i in intervalid:
            if '\infty' in i and i[0] != '-\infty':
                kasvab_parameeter = True
                for arv in range(math.ceil(i[0]), 30):
                    if diff(sisend).replace('x', '('+str(arv)+')') < 0:
                        kasvab_parameeter = False
                    else:
                        kasvab_parameeter = True
                if kasvab_parameeter:
                    kasvab.append(i)
            if '-\infty' in i and i[1] != '\infty':
                kasvab_parameeter = True
                for arv in range(-30, math.floor(i[1])):
                    if diff(sisend).replace('x', '('+str(arv)+')') < 0:
                        kasvab_parameeter = False
                    else:
                        kasvab_parameeter = True
                if kasvab_parameeter:
                    kasvab.append(i)
            if '\infty' not in i and '-\infty'not in i:
                kasvab_parameeter = True
                for arv in range(math.ceil(i[0]), math.floor(i[1])):
                    if diff(sisend).replace('x', '('+str(arv)+')') < 0:
                        kasvab_parameeter = False
                    else:
                        kasvab_parameeter = True
                if kasvab_parameeter:
                    kasvab.append(i)

        return list(map(str, list(kasvab)))
    else:
        return ['Puudub']


def leia_kahanemine(sisend):
    if diff(diff(sisend, x), x) != 0:
        vaheldus_piirkond = solve(diff(sisend))
        algne_list = ['-\infty', '\infty']

        for i in range(len(vaheldus_piirkond)):
            algne_list.insert(1, vaheldus_piirkond[i-1])

        intervalid = []
        for paar in paarideks(algne_list):
            intervalid.append(paar)

        kahaneb = []
        for i in intervalid:
            if '\infty' in i and i[0] != '-\infty':
                kahaneb_parameeter = True
                for arv in range(math.ceil(i[0]), 30):
                    if diff(sisend).replace('x', '('+str(arv)+')') > 0:
                        kahaneb_parameeter = False
                    else:
                        kahaneb_parameeter = True
                if kahaneb_parameeter:
                    kahaneb.append(i)
            if '-\infty' in i and i[1] != '\infty':
                kahaneb_parameeter = True
                for arv in range(-30, math.floor(i[1])):
                    if diff(sisend).replace('x', '('+str(arv)+')') > 0:
                        kahaneb_parameeter = False
                    else:
                        kahaneb_parameeter = True
                if kahaneb_parameeter:
                    kahaneb.append(i)
            if '\infty' not in i and '-\infty'not in i:
                kahaneb_parameeter = True
                for arv in range(math.ceil(i[0]), math.floor(i[1])):
                    if diff(sisend).replace('x', '('+str(arv)+')') > 0:
                        kahaneb_parameeter = False
                    else:
                        kahaneb_parameeter = True
                if kahaneb_parameeter:
                    kahaneb.append(i)
        if len(kahaneb) > 0:
            return list(map(str, list(kahaneb)))
        else:
            return ['Puudub']
    else:
        return ['Puudub']


def leia_kumerus(sisend):
    if diff(diff(sisend, x), x) != 0:
        if 'x' not in str(diff(diff(sisend, x), x)):
            if float(diff(diff(sisend, x), x)) < 0:
                return ['-\infty', '\infty']
        if 'x' in str(diff(diff(sisend, x), x)):
            vaheldus_piirkond = solve(diff(diff(sisend, x), x))
            algne_list = ['-\infty', '\infty']

            for i in range(len(vaheldus_piirkond)):
                algne_list.insert(1, vaheldus_piirkond[i-1])

            intervalid = []
            for paar in paarideks(algne_list):
                intervalid.append(paar)

            kumer = []
            for i in intervalid:
                if '\infty' in i and i[0] != '-\infty':
                    kumer_parameeter = True
                    for arv in range(math.ceil(i[0]), 30):
                        if diff(diff(sisend, x), x).replace('x', '('+str(arv)+')') > 0:
                            kumer_parameeter = False
                        else:
                            kumer_parameeter = True
                    if kumer_parameeter:
                        kumer.append(i)
                if '-\infty' in i and i[1] != '\infty':
                    kumer_parameeter = True
                    for arv in range(-30, math.floor(i[1])):
                        if diff(diff(sisend, x), x).replace('x', '('+str(arv)+')') > 0:
                            kumer_parameeter = False
                        else:
                            kumer_parameeter = True
                    if kumer_parameeter:
                        kumer.append(i)
                if '\infty' not in i and '-\infty'not in i:
                    kumer_parameeter = True
                    for arv in range(math.ceil(i[0]), math.floor(i[1])):
                        if diff(diff(sisend, x), x).replace('x', '('+str(arv)+')') > 0:
                            kumer_parameeter = False
                        else:
                            kumer_parameeter = True
                    if kumer_parameeter:
                        kumer.append(i)
            if len(kumer) > 0:
                return list(map(str, list(kumer)))
            else:
                return ['Puudub']
        else:
            return ['Puudub']
    else:
        return ['Puudub']


def leia_nõgusus(sisend):
    if diff(diff(sisend, x), x) != 0:
        if 'x' not in str(diff(diff(sisend, x), x)):
            if float(diff(diff(sisend, x), x)) > 0:
                return ['-\infty', '\infty']
        if 'x' in str(diff(diff(sisend, x), x)):
            vaheldus_piirkond = solve(diff(diff(sisend, x), x))
            algne_list = ['-\infty', '\infty']

            for i in range(len(vaheldus_piirkond)):
                algne_list.insert(1, vaheldus_piirkond[i-1])

            intervalid = []
            for paar in paarideks(algne_list):
                intervalid.append(paar)

            nõgus = []
            for i in intervalid:
                if '\infty' in i and i[0] != '-\infty':
                    nõgus_parameeter = True
                    for arv in range(math.ceil(i[0]), 30):
                        if diff(diff(sisend, x), x).replace('x', '('+str(arv)+')') < 0:
                            nõgus_parameeter = False
                        else:
                            nõgus_parameeter = True
                    if nõgus_parameeter:
                        nõgus.append(i)
                if '-\infty' in i and i[1] != '\infty':
                    nõgus_parameeter = True
                    for arv in range(-30, math.floor(i[1])):
                        if diff(diff(sisend, x), x).replace('x', '('+str(arv)+')') < 0:
                            nõgus_parameeter = False
                        else:
                            nõgus_parameeter = True
                    if nõgus_parameeter:
                        nõgus.append(i)
                if '\infty' not in i and '-\infty'not in i:
                    nõgus_parameeter = True
                    for arv in range(math.ceil(i[0]), math.floor(i[1])):
                        if diff(diff(sisend, x), x).replace('x', '('+str(arv)+')') < 0:
                            nõgus_parameeter = False
                        else:
                            nõgus_parameeter = True
                    if nõgus_parameeter:
                        nõgus.append(i)
            if len(nõgus) > 0:
                return list(map(str, list(nõgus)))
            else:
                return ['Puudub']
        else:
            return ['Puudub']
    else:
        return ['Puudub']


def leia_käänupunkt(sisend):
    if diff(diff(sisend, x), x) != 0 and not str(diff(diff(sisend, x), x)).isnumeric():
        vastus = []
        nullkohad = solve(diff(diff(sisend, x), x))
        for i in nullkohad:
            vastus.append((i, eval(sisend.replace('x', '('+str(i)+')'))))
        return list(map(str, vastus))
    else:
        return ['Puudub']


def lisa_graafik(formula):
    fig = pl.figure()
    ax = fig.add_axes([0.1, 0.2, 0.4, 0.4])
    x = np.arange(-10, 10, 0.1)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    y = eval(formula)
    ax.plot(x, y)
    pl.grid()
    pl.xticks(np.arange(-10,10,1))
    pl.yticks(np.arange(-10,10,1))
    pl.ylim(-10, 10)
    fig.set_size_inches(17, 12)
    x = symbols('x')

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')


    funktsioon = latex(eval(formula))

    nullkohad = latex(' , '.join(leia_nullkohad(formula)))
    if 'Puudub' in nullkohad:
        nullkohad = latex(' , '.join(leia_nullkohad(formula)))
    else:
        nullkohad = latex(eval(' , '.join(leia_nullkohad(formula))))

    miinimum = latex(' , '.join(leia_miinimum(formula)))
    if 'Puudub' in miinimum:
        miinimum = latex(' , '.join(leia_miinimum(formula)))
    else:
        miinimum = latex(eval(' , '.join(leia_miinimum(formula))))

    maksimum = latex(' , '.join(leia_maksimum(formula)))
    if 'Puudub' in maksimum:
        maksimum = latex(' , '.join(leia_maksimum(formula)))
    else:
        maksimum = latex(eval(' , '.join(leia_maksimum(formula))))

    formatkasvab = ''.join(ch for ch, _ in itertools.groupby(''.join(leia_kasvamine(valem.get()))))
    formatkahaneb = ''.join(ch for ch, _ in itertools.groupby(''.join(leia_kahanemine(valem.get()))))
    formatkumerus = ''.join(ch for ch, _ in itertools.groupby(''.join(leia_kumerus(valem.get()))))
    formatnõgusus = ''.join(ch for ch, _ in itertools.groupby(''.join(leia_nõgusus(valem.get()))))
    formatkäänukoht = ''.join(ch for ch, _ in itertools.groupby(''.join(leia_käänupunkt(valem.get()))))

    # TODO:
    # eval ei tööta siis, kui asja sees on string, näiteks 'puudub' või 'infty'
    # evalile ei meeldi, kui stringis on \ sümbol
    # eval tagastab floate päris haige komakohaga

    kasvab = formatkasvab.replace("'", "")
    kahaneb = formatkahaneb.replace("'", "")
    kumerus = formatkumerus.replace("'", "")
    nõgusus = formatnõgusus.replace("'", "")
    käänukoht = formatkäänukoht.replace("'", "")

    plt.title('$%s$' % funktsioon, fontsize=25)
    data1 = ('Nullkohad: ' + '\n' + '$%s$' % nullkohad)
    data2 = ('Miinimumkohad: ' + '\n' + '$%s$' % miinimum)
    data3 = ('Maksimumkohad: ' + '\n' + '$%s$' % maksimum)
    data4 = ('Kasvamispiirkond:' + '\n' + '$%s$' % kasvab)
    data5 = ('Kahanemispiirkond:' + '\n' + '$%s$' % kahaneb)
    data6 = ('Kumeruspiirkond:' + '\n' + '$%s$' % kumerus)
    data7 = ('Nõgususpiirkond:' + '\n' + '$%s$' % nõgusus)
    data8 = ('Käänukohad:' + '\n' + '$%s$' % käänukoht)

    pl.text(11, 8, data1)
    pl.text(11, 5.5, data2)
    pl.text(11, 3, data3)
    pl.text(11, 0.5, data4)
    pl.text(11, -2, data5)
    pl.text(11, -4.5, data6)
    pl.text(11, -7, data7)
    pl.text(11, -9.5, data8)

    pl.savefig('graafik.png', bbox_inches='tight')

    global img
    img = PhotoImage(file="graafik.png")
    graaf = Label(image=img)
    graaf.image = img
    graaf.pack(side=BOTTOM)



def näita_tulemus():
    if valem.get() != '':

        lisa_graafik(valem.get())

    else:
        tühi_sisend = ttk.Label(raam, text='Sisend on tühi.')
        tühi_sisend.place(x=150, y=240)

def on_closing():
    if os.path.isfile('graafik.png'):
        os.remove('graafik.png')
        sys.exit()
    else:
        sys.exit()


def restart():
    img.destroy()

while True:
    raam = Tk()
    raam.title('PLOTMASTER BASIC BETA 1.1')

    background_image=PhotoImage(file="bgV2.gif")
    background_label = Label(raam, image=background_image)
    background_label.place(x=-0, y=0)

    raam.configure(background='white')

    laius = 1300
    kõrgus = 750

    ekraanilaius = raam.winfo_screenwidth()
    ekraanikõrgus = raam.winfo_screenheight()

    xkord = (ekraanilaius/2) - (laius/2)
    ykord = (ekraanikõrgus/2) - (kõrgus/2)

    raam.geometry('%dx%d+%d+%d' % (laius, kõrgus, xkord, ykord))

    global valem
    valem = ttk.Entry(raam, width=40)
    valem.place(x=laius/2.53, y=70, width=265, height=60)

    arvuta_nupp = ttk.Button(raam, text='Arvuta!', command=näita_tulemus)
    arvuta_nupp.place(x=laius/2.53, y=140, width=130, height=40)

    uus_funktsioon = ttk.Button(raam, text='Uus funktsioon', command=restart)
    uus_funktsioon.place(x=laius/2.0, y=140, width=130, height=40)

    raam.mainloop()

