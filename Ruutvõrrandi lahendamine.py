from tkinter import *
from math import sqrt

def otsi():
    a = sis_a.get()
    b = sis_b.get()
    c = sis_c.get()

    
    if a == "" or b == "" or c == "":
        sis_a.config(bg="red" if a == "" else "lightblue")
        sis_b.config(bg="red" if b == "" else "lightblue")
        sis_c.config(bg="red" if c == "" else "lightblue")
        tulemus.config(text="täitke kõik väljad!", bg="yellow")
        return

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        tulemus.config(text="Sisestage ainult numbrid!", bg="orange")
        return

    
    D = b * b - 4 * a * c
    vastus = "D = " + str(D) + "\n"

    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        vastus += "2 juurt: x1 = " + str(round(x1, 2)) + ", x2 = " + str(round(x2, 2))
    elif D == 0:
        x = -b / (2 * a)
        vastus += "1 juur: x = " + str(round(x, 2))
    else:
        vastus += "Pole juuri"

    tulemus.config(text=vastus, bg="yellow")


aken = Tk()
aken.title("Teema 8")
aken.geometry("600x300")
aken.configure(bg="lightblue")

pealkiri = Label(aken, text="Ruutvõrrandi lahendamine", bg="lightblue", fg="green", font=("Arial", 16))
pealkiri.pack(pady=10)

sisend = Frame(aken, bg="lightblue")
sisend.pack()

sis_a = Entry(sisend, width=5, bg="lightblue", font=("Arial", 14))
sis_a.grid(row=0, column=0)
Label(sisend, text="x² +", bg="lightblue", font=("Arial", 14)).grid(row=0, column=1)

sis_b = Entry(sisend, width=5, bg="lightblue", font=("Arial", 14))
sis_b.grid(row=0, column=2)
Label(sisend, text="x +", bg="lightblue", font=("Arial", 14)).grid(row=0, column=3)

sis_c = Entry(sisend, width=5, bg="lightblue", font=("Arial", 14))
sis_c.grid(row=0, column=4)
Label(sisend, text="= 0", bg="lightblue", font=("Arial", 14)).grid(row=0, column=5)

nupp = Button(sisend, text="Решить", command=otsi, bg="darkgreen", fg="white", font=("Arial", 14))
nupp.grid(row=0, column=6, padx=10)

tulemus = Label(aken, text="Решение", bg="yellow", font=("Arial", 12), width=60, height=4)
tulemus.pack(pady=20)

aken.mainloop()




import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-8, 13, 50)

y = (x - 2.5)**2

plt.plot(x, y, 'bo') # 'bo' - синве кружочки
plt.plot(2.5, 0, 'go') 

plt.title("Квадратное уравнение")
plt.xlabel("x")
plt.ylabel("y")


