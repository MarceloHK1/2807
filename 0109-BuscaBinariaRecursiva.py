class Busca:

    def __init__(self, lista):
        self.lista = lista

    def buscar(self, numero, inicio=0, fim=None):
        if fim == None:
            fim = len(self.lista) - 1

        if inicio > fim:
            return -1

        meio = (inicio + fim) // 2

        if numero == self.lista[meio]:
            return meio
        elif numero < self.lista[meio]:
            return self.buscar(numero, inicio, meio - 1)
        else:
            return self.buscar(numero, meio + 1, fim)


listagem = []
tamanho = int(input("Digite o tamanho da lista: "))

while tamanho > 0:
    tamanho -= 1
    elemento = int(input("Digite o elemento a ser adicionado na lista: "))
    listagem.append(elemento)

listagem.sort()

num_procurado = int(input("Digite o número que deseja encontrar: "))

buscador = Busca(listagem)
resultado = buscador.buscar(num_procurado)

if resultado != -1:
    print("O número {} foi encontrado na posição {}.".format(num_procurado, resultado))
else:
    print("O número não foi encontrado.")
