    
import time
def mostrar_menu():
    time.sleep(2)
    print("----- Menú -----")
    print("1. Print first 10 natural numbers using while loop")
    print("2. The same in reverse order")
    print("3. Print first 10 natural numbers using for loop")
    print("4. The same in reverse order")
    print("5. Input a number and print its multiplication table")
    print("6.Growing numbers")
    print("7.Growing numbers -")
    print("8.Inverse")
    print("10.Inverse -")
    print("11. Input a number and calculate the sum of all numbers from 1 to a given number. For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)")
    print("12. Given a list of numbers = [7, 8, 12, 29, 75, 150, 180, 145, 525, 50] print those that are divisible by 4 or by 5.")
    print("13. The same but stop the loop if a number is not greater that its predecessor.")
    print("14.SALIR")
    global opcion
    opcion = input("Elige una opción (1-2, 12 para salir): ")

def one():
    i = 1
    while i < 11:
        print(i)
        i += 1

def two():
    i = 10
    while i > 0:
        print(i)
        i -= 1

def three():
    for i in range(1, 11):
        print(i)

def four():
    for i in range(10, 0,-1):
        print(i)

def five():
    numerin = input("Esctibe un numero: ")
    for i in range(1, 11):
        print(numerin, "X", i, "=", int(numerin) * i)

def six():
    suma = 0
    while True:
        try:
            numerin = int(input("Escribe un número (0 para terminar): ")) 
            if numerin != 0:
                suma += numerin
            else:  
                print("Se ha introducido el 0, este es el resultado de la suma:")
                print(suma)
                break
        except ValueError: 
            print("Error: Por favor, introduce un número entero.")
    
def seven(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()

def eight(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
            if j < i:
                print("-",end="")
        print()

def nine(n):
    n += 1
    for i in range(n, 0, -1):
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def ten(n):
    n += 1
    for i in range(n, 0, -1):
        for j in range(i - 1, 0, -1):
            print(j, end="")
            if j > 1:
                print("-", end="")
        print()

def eleven(numero):
    suma = 0
    for i in range(1,  numero + 1):
        suma += i
    print(suma)


numeross = [7, 8, 12, 29, 75, 150, 180, 145, 525, 50]

def twelve():
    x  = 0

    for i in numeross:
        x == i
        if i % 4 == 0 or i % 5 == 0:
            print(i)


def therteen():
    x = 0
    for i in numeross:

        if i < x:
            break    
        else:
            x = i
            if i % 4 == 0 or i % 5 == 0:
                print(i)


while True:  
    mostrar_menu()
    if opcion == "1":
        one()
    elif opcion == "2":
        two()
    elif opcion == "3":
        three()
    elif opcion == "4":
        four()
    elif opcion == "5":
        five()
    elif opcion == "6":
        six()
    elif opcion == "7":
        seven(int(input("Introduce el numero maximo de la piramide: ")))
    elif opcion == "8":
        eight(int(input("Introduce el numero maximo de la piramide: ")))
    elif opcion == "9":
        nine(int(input("Introduce el numero maximo de la piramide: ")))
    elif opcion == "10":
        ten(int(input("Introduce el numero maximo de la piramide: ")))
    elif opcion == "11":
        eleven(int(input("Introduce el numero maximo de la piramide: ")))
    elif opcion == "12":
        twelve()
    elif opcion == "13":
        therteen()
    elif opcion == "14":
        print("Saliendo del programa.")
        break  # Salir del bucle si elige la opción 12
    else:
        print("Opción no válida. Intenta de nuevo.")
