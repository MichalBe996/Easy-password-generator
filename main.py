import string
import tkinter
import random
from tkinter import messagebox
lista_liczb = [x for x in range (10)]
lista_male = list(string.ascii_lowercase)
lista_duze = list(string.ascii_uppercase)


def silne_haslo():
    haslo = []
    for x in range(5):
        haslo.append(random.choice(lista_duze))
        haslo.append(random.choice(lista_male))
        haslo.append(random.choice(lista_liczb))
    random.shuffle(haslo)
    messagebox.showinfo("Nowe hasło", haslo)
def slabe_haslo():
    haslo = []
    for x in range(3):
        haslo.append(random.choice(lista_duze))
        haslo.append(random.choice(lista_male))
        haslo.append(random.choice(lista_liczb))
    random.shuffle(haslo)
    messagebox.showinfo("Nowe hasło", haslo)

root = tkinter.Tk()
root.title("Generator haseł")
root.geometry("300x200")
label_1 = tkinter.Label(text = "Wybierz siłę hasła: ")
button_str = tkinter.Button(root, text = "Silne", height = 5, width = 10, command = silne_haslo)
button_weak = tkinter.Button(root, text = "Słabe", height = 5, width = 10, command = slabe_haslo)
label_1.place(x = 100, y = 40)
button_str.place(x = 50, y = 60)
button_weak.place(x = 150, y = 60)


root.mainloop()