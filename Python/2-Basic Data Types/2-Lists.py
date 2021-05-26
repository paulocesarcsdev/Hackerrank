#https://www.hackerrank.com/challenges/python-lists/problem

lista = []


n = int(input('Entre com o elemento: '))

for i in range(n):
    #print(i+1)
    lista.append(i)

print(lista)
del lista[0]
print(lista)
armazena = lista.pop(0)
lista.append(armazena)
print(lista)
lista.sort()
print(lista)
armazena2 = lista.pop(-1)
print(armazena2)