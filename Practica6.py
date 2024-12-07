nombrARCH = input("Nombre del archivo: ")
with open(nombrARCH, 'r') as file:
    content = file.read()
simbolitos = "!?.:;,()[]{}-\"'<>/\\|&*%@#~_^+=`$"
quitar_simbolitos = ''.join(char if char not in simbolitos else ' ' for char in content)

words = quitar_simbolitos.split()

d = dict()

for word in words:
    word = word.lower() 
    if word in d:
            d[word] += 1
    else:
            d[word] = 1

print("Frecuencia de palabras:")
for word, count in d.items():
    print(word + ": " + str(count))