import time
myset = set()
big_techs = {'google', 'amazon', 'apple', 'microsoft'}
def one():
    print("----------------------")
    print(myset)
    menu()

def two():
    print("----------------------")
    myset.clear()
    print("You cleaned myset")
    menu()

def three():
    print("----------------------")
    myset.add(input("Introduce elemento:"))
    menu()

def four():
    print("----------------------")
    x = input("Introduce elemento para borrar:")
    try:
        myset.remove(x) 
    except KeyError:
        print("Está vacío o el elemento no existe.")
    menu()

def five():
    print("----------------------")
    try:
        elemento = myset.pop()
    except KeyError:
        print("Esta vacio")
    menu()

def six():
    print("----------------------")
    x = input("Escribe el elemento que deseas comprobar: ")
    found = False
    for i in myset:
        if i == x:
            print("Si existe")
            found = True
            break

    if not found:
        print("No existe")
    menu()

def seven():
    print("----------------------")
    myset.update({"apple", "banana", "cherry", "lemon"})
    menu()

def eight():
    print("----------------------")
    myset = myset - big_techs
    menu()

def nine():
    print("----------------------")
    for o in myset:
        print(o.upper())
    menu()

def ten():
    print("----------------------")
    exit()
    menu()




def menu():
    print("----------------------")
    time.sleep(1)
    print("MENU")
    print("1. Display all items")
    print("2. Clear")
    print("3. Add an item")
    print("4. Remove an item (avoid runtime errors)")
    print("5. Pop an item (avoid runtime errors)")
    print("6. Check if an item exists")
    print("7. Add some fruits { \"apple\", \"banana\", \"cherry\", “lemon” }")
    print("8. Subtract some big-techs { “google”, “amazon”, “apple”, “microsoft”}")
    print("9. Display all items in capital letters")
    print("10. Exit")
    opcion = input("Introduzca el numero de la accion: ")
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
        seven()
    elif opcion == "8":
        eight()
    elif opcion == "9":
        nine()  
    elif opcion == "10":
        ten() 
    else:
        print("Opción no válida. Intenta de nuevo.")
        time.sleep(1.5)
        menu()

menu()