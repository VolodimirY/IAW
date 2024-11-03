import time
tupple= (1, 0, 33, 10, 10, 20, 14)

def one():
    print("1. The sum of the elements.")
    x = 0
    for i in tupple:
        x += i
    print(x)
    time.sleep(1.5)
    menu()

def two():
    print("2. The smallest element.")
    x = 1000000000000
    for i in tupple:
        if i < x:
            x = i
    print(x)
    time.sleep(1.5)
    menu()

def  three():
    print("3. The largest element.")
    x = -100000000000
    for i in tupple:
        if  i > x:
            x = i
    print(x)
    time.sleep(1.5)
    menu()

def four():
    print("4. How many elements are multiple of the number passed as second argument.")
    n = int(input("Introduce el segundo munero:"))
    count = 0
    for i in tupple:
        if i % n == 0:
            count  += 1
            print("El elemento"   , i , "es múltiplo de" , n)
    print("En total"  , count , "son múltiplos de" , n)
    time.sleep(1.5)
    menu()

def five():
    print("5. An object with sum, count, avg, max and min from the elements.")
    stats = {
        'sum': sum(tupple),
        'count': len(tupple),
        'len': len(tupple),
        'avg': sum(tupple) / len(tupple),
        'max': max(tupple),
        'min': min(tupple),
    }
    print(stats)
    time.sleep(1.5)
    menu()

def six():
    print("6. Nothing, but order the tuple and eliminate duplicates.")
    tupple_sorted = sorted(tupple)
    tupple_sorted_sindup = []
    for i in tupple_sorted:
        if i not in tupple_sorted_sindup:
            tupple_sorted_sindup.append(i)
    print(tupple_sorted_sindup)
    time.sleep(1.5)
    menu()       

def seven():
    print("7. Nothing, but reverse the tuple")
    tupple_reversa = []
    for i in tupple:
        tupple_reversa.insert(0, i)
    print(tupple_reversa)
    time.sleep(1.5)
    menu()

def eight():
    print("8. A copy of the tuple ordered and without duplicates. Don’t change the original tuple.")
    print(sorted(set(tupple)))
    time.sleep(1.5)
    menu()

def nine():
    print("9. True if all the tuple elements are the same, otherwise return false.")
    tupple_vacia = []
    for i in tupple:
        tupple_vacia.append(tupple[0])
    if tuple(tupple_vacia) == tupple:
        return True
    else: 
        return False


def ten():
    print("10. True if all the tuple elements are greater than the number passed as second parameter.")
    x = int(input("Introduce un numero: "))
    for i in tupple:
        if x > i:
            return False
    return True

def menu():
    print("Esta es la tupla plincipal", tupple)
    opcion = input("Introduzca el numero del ejercicio: ")
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
        print(nine())
        time.sleep(1.5)
        menu()
    elif opcion == "10":
        print(ten())
        time.sleep(1.5)
        menu()
    else:
        print("Opción no válida. Intenta de nuevo.")
        time.sleep(1.5)
        menu()

menu()