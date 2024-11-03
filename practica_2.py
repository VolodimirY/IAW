    
from sqlite3 import IntegrityError
import time
def mostrar_menu():
    time.sleep(2)
    print("----- Menú -----")
    print("Write some functions that take a list of integers as argument and return the following:")
    print(". The sum of the elements.")
    print("2. The smallest element.")
    print("3. The largest element")
    print("4. How many elements are multiple of the number passed as second argument.")
    print("5. An object with sum, count, avg, max and min from the elements.")
    print("6. A copy of the list ordered without duplicates, using sort() and pop() methods.")
    print("7. The same as exercise 5, after adding the element passed as second argument.")
    print("8. The same as exercise 5, after deleting the element passed as second argument")
    print("9. The same as exercise 5, after adding the elements of the list passed as second argument")
    print("10. The element more repeated, using count() method. In case of tie, return the first one")
    print("11. Similar to exercise 6, but don’t return anything. Just order the original list and eliminate duplicates. Call the function in order to check that the list is passed by reference to the function.")
    print("14.SALIR")
    global opcion
    opcion = input("Elige una opción (1-2, 12 para salir): ")
integers = [12,37,2,2,1,11,25,6]
def one():
    x = 0 
    for i in integers:
        x +=  i
    print(x)


def two():
    x = 100 
    for i in integers:
        if i < x:
            x = i
    print(x)

def three():
    x = 0 
    for i in integers:
        if i > x:
            x = i
    print(x)

def four(argumento):
    count = 0
    for i in integers:
        if i % argumento == 0:
            count += 1
    print(count)

def five():
    stats={
    'sum': sum(integers),
    'len': len(integers),
    'avg' : sum(integers) / len(integers),
    "max" : max(integers),
    "min" : min(integers),
}
    print(stats)

def six():
    integers_copy = integers.copy()
    integers_copy.sort()
    unique_list = []
    while integers_copy:
        current = integers_copy.pop()
        if not unique_list or unique_list[-1] != current:
            unique_list.append(current)
    print(unique_list) 

def seven(integers):
    new_element = int(input("Introduce el nuevo elemento a añadir: "))
    integers.append(new_element)
    stats = {
        'sum': sum(integers),
        'len': len(integers),
        'avg': sum(integers) / len(integers),
        'max': max(integers),
        'min': min(integers),
    }
    print(stats)
        


def eight(integers, element_to_remove):
    if element_to_remove in integers:
        integers.remove(element_to_remove)
    stats = {
        'sum': sum(integers),
        'len': len(integers),
        'avg': sum(integers) / len(integers) if integers else 0,
        'max': max(integers) if integers else None,
        'min': min(integers) if integers else None,
    }
    print(stats)

def nine(integers, new_list):
    integers.extend(new_list)
    stats = {
        'sum': sum(integers),
        'len': len(integers),
        'avg': sum(integers) / len(integers) if integers else 0,
        'max': max(integers) if integers else None,
        'min': min(integers) if integers else None,
    }
    print(stats)

def ten():
    cuenta = 0
    repe = None
    for i in integers:
        current_count = integers.count(i)
        if current_count > cuenta:
            cuenta = current_count
            repe = i
    print(repe)

def eleven():
    integers.sort()
    listilla = []
    for i in integers:
        if not listilla or listilla[-1] != i:
            listilla.append(i)
    integers.clear()
    integers.extend(listilla)


while True:  
    mostrar_menu()
    if opcion == "1":
        one()
    elif opcion == "2":
        two()
    elif opcion == "3":
        three()
    elif opcion == "4":
        four(int(input("Introduce el argumento: ")))
    elif opcion == "5":
        five()
    elif opcion == "6":
        six()
    elif opcion == "7":
        seven(integers)
    elif opcion == "8":
        element_to_remove = int(input("Introduce el elemento a eliminar: "))
        eight(integers, element_to_remove)
    elif opcion == "9":
        new_list = list(map(int, input("Introduce la lista de números a añadir (separados por espacios): ").split()))
        nine(integers, new_list)
    elif opcion == "10":
        ten()
    elif opcion == "11":
        eleven()
        print("La lista ha sido ordenada y los duplicados eliminados.")
        print("Lista actual:", integers) 
    elif opcion == "14":
        print("Saliendo del programa.")
        break 
    else:
        print("Opción no válida. Intenta de nuevo.")





