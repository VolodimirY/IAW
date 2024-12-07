import time
d = dict()
s = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''


def one():
    print(d)
    menu()

def two():
    for i in s:
        print(i)
    menu()

def three():
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    menu()

def four():
    print(list(d.keys()))
    menu()

def five():
    print(sorted(d.keys()))
    menu()

def six():
    sorted_keys = sorted(d.keys())
    keys_desc = []
    for i in range(len(sorted_keys) - 1, -1, -1):
        keys_desc.append(sorted_keys[i])
    print(keys_desc)
    menu()

def six2(): # he encontrado una alternativa a six()
    print(sorted(d.keys(), reverse=True))
    menu()

def seven():
    print(list(d.values()))
    menu()

def eight():
    print(sorted(d.values()))
    menu()

def nine():
    sorted_values = sorted(d.values())
    values_desc = []
    for i in range(len(sorted_values) - 1, -1, -1):
        values_desc.append(sorted_values[i])
    print(values_desc)
    menu()

def nine2(): #la opcion con reverse
    print(sorted(d.values(), reverse=True))
    menu()

def ten():
    print(list(d.items()))
    menu()

def eleven():
    print(sorted(d.items()))
    menu()

def twelve():
    sorted_items = sorted(d.items())
    items_desc = []
    for i in range(len(sorted_items) - 1, -1, -1):
        items_desc.append(sorted_items[i])
    print(items_desc)
    menu()

def twelve2():
    print(sorted(d.items(), reverse=True))
    menu()


def menu():
    time.sleep(1)
    print("-------------")
    print("1 The whole string")
    print("2 The string, one character per line")
    print("3 The number of repetitions for each character. How-to: for each character, add (or update) an item to the dictionary where the key is the character and the value is the number of repetitions, and finally print the dictionary.")
    print("4 Keys unordered")
    print("5 Keys ordered")
    print("6 Keys in descending order")
    print("7 Values unordered")
    print("8 Values ordered")
    print("9 Values in descending order")
    print("10 Items unordered ")
    print("11 Items ordered by key")
    print("12 Items in descending order by key")
    print("13 Items ordered by value")
    print("14 Items in descending order by value")
    print("15 Quit")
    print("-------------")
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
        nine()
    elif opcion == "10":
        ten()
    elif opcion == "11":
        eleven()
    elif opcion == "12":
        twelve()
    elif opcion == "15":
       exit 
    else:
        print("Opción no válida. Intenta de nuevo.")

        menu()

menu()