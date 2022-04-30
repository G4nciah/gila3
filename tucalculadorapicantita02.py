import sys

n1 = 0
n2 = 0

menu = """
1-Sumar
2-Restar
3-Multiplicar
4-Dividir
0-Salir
"""

def Sumar():
    print("ingresa un numero:")
    n1 = float(input())
    print("ingresa un sumando:")
    n2 = float(input())
    print("resultado:", n1 + n2)

def Restar():
    print("ingresa un numero:")
    n1 = float(input())
    print("ingresa un sustraendo:")
    n2 = float(input())
    print("resultado:", n1 - n2)

def Multiplicar():
    print("ingresa un numero:")
    n1 = float(input())
    print("ingresa un producto:")
    n2 = float(input())
    print("resultado:", n1 * n2)

def Dividir():
    print("ingresa un numero:")
    n1 = float(input())
    print("ingresa un divisor:")
    n2 = float(input())
    print("resultado:", n1 / n2)     


print("Esta es tu calculadora picantita")
while True:
    print(menu)
    opc = int(input())
    if opc == 1:
        Sumar()
    elif opc == 2:
        Restar()
    elif opc == 3:
        Multiplicar()
    elif opc == 4:
        Dividir()
    elif opc == 0:
        sys.exit()   
    