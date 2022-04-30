from asyncore import loop
import os 
from importlib.resources import open_text
from re import A
from tkinter import OptionMenu
from webbrowser import open_new_tab


print("Hola")
nombre = input("nombre:")
edad=input("edad:")
if int(edad) >=18: 
    os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley") 