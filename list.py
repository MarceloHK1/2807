lista = []
tamanho_lista = int(input("Digite a quantidade de numeros da lista: "))
while len(lista) < tamanho_lista:
    num = int(input("Digite um numero para a lista: "))
    lista.append(num)

maior = lista[0]
menor = lista[0]
soma = 0

for numeros in lista:                                                               # usando For
    if numeros > maior:
        maior = numeros
    elif numeros < menor:
        menor = numeros

    soma += numeros
print("O menor é {}, o maior é {} e a soma é {}".format(menor, maior, soma))


lista_2 = []
tamanho_lista_2 = int(input("Digite a quantidade de numeros da lista: "))
while len(lista_2) < tamanho_lista_2:
    num = int(input("Digite um numero para a lista: "))
    lista_2.append(num)
tamanho = len(lista_2)
indice = 0
maior_2 = lista_2[0]
menor_2 = lista_2[0]
soma_2 = 0

while tamanho > 0:                                                                  # usando while
    numero = lista_2[indice]

    if numero > maior_2:
        maior_2 = numero
    elif numero < menor_2:
        menor_2 = numero

    soma_2 += numero
    indice += 1
    tamanho -= 1

print("O menor é {}, o maior é {} e a soma é {}".format(menor_2, maior_2, soma_2))

for x in range(0, 3):                                               # range(inicio, fim)
    print(lista[x])

a = "abcd"
c = a*4
quantidade_c = 0
for letras in c:
    if letras == "c":
        quantidade_c += 1
print(quantidade_c)