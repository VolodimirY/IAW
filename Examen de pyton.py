
#VOLODIMIR YARMASH YARMASH, EXAMEN A 
def primero():
    entero = int(input("Escriba un número entero: "))
    entero2 = int(input("Escriba un número entero mayor o igual que " + str(entero) + ": "))

    if entero > entero2 or entero2 == entero :
        print("Error: el segundo número no es mayor o igual que " + str(entero))
        print("Game over")
    elif entero < entero2:
        for num in range(entero, entero2 + 1):
            if num % 2 == 0:
                print("El número : " + str(num) + " es par")
        else:
                print("El número : " + str(num) + " es impar")
        print("Game over")

#primero()
def segundo():
    es_in = {'rosa': 'rose', 'hola': 'hello', 'amor': 'love', 'coche': 'car'}
    
    while True:
        palabra = input("Escriba una palabra: ")
        if palabra == "fin":
            print("Game Over")
            break
        elif palabra in es_in:
            print(es_in[palabra])
        else:
            print("not found")
#segundo()
