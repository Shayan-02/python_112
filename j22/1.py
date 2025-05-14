from random import choice
from tkinter import filedialog

f = open("./j22/test.txt")

person = f.readlines()

print(choice(person))

