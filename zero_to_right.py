lista = [1, 2, 0, 0, 5, 0, 1]

def zero_to_the_right(lista):
    for _ in range(lista.count(0)):
        lista.append(lista.pop(lista.index(0)))

zero_to_the_right(lista)
print(lista)
