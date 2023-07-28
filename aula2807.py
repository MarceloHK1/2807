import os

x1 = os.listdir()                       #returns a list containing the names of the entries in the directory given by path and opens the files in self

for file in x1:                         #percorre a lista de arquivos e diretorios
    print(file)                         #printa os arquivos e diretorios         

numeros = [1, 2, 3, 4]                              #faz uma lista de inteiros
for posicao, numero in enumerate(numeros):          #percorre a posicao e o numero de cada elemento da lista de inteiros
    if numero == 4:
        print(posicao + 1)


frutas = ['pera', 'uva', 'maça', 'mamao']
for fruta in frutas:
    print (fruta)

print(frutas)

numeros = [1, 2, 3, 4, 0, 60]
print("o tamanho da lista é", len(numeros))         #tamanho da lista  
print(sum(numeros))                                 #soma dos elementos da lista
print(max(numeros))                                 #maior num da lista
print(min(numeros))                                 #menor num da lista
print(numeros[::-1])                                #reverter a lista
numeros.append(50)                                  #adiciona um elemento na última posição