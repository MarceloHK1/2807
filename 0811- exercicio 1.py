def tranformar_nota(nota):

    if nota >= 9.0:
        new_grade = "A"
    elif nota >= 8.0:
        new_grade = "B"
    elif nota >= 7.0:
        new_grade = "C"
    elif nota >= 5.0:
        new_grade = "D"
    elif nota >= 3.0:
        new_grade = "E"
    else:
        new_grade = "F"

    return new_grade


def perguntar_nota():
    notadoaluno = float(input("Digite a nota do aluno: "))
    return notadoaluno


def perguntar_nome():
    nome = input("Digite o nome do aluno: ")
    return nome


def tamanho_da_lista():
    tamanho = int(input("Digite o tamanho da lista: "))
    return tamanho


def adicionar_na_lista(lista, nota):
    lista.append(nota)


def printar_resultado(a, b, c):
    print(a, '       ', b, '       ', c)


if __name__ == "__main__":
    listadenotas = []
    listadegrades = []
    listadenomes = []
    i = tamanho_da_lista()
    while i > 0:
        nomedoaluno = perguntar_nome()
        notadoaluho = perguntar_nota()
        nova_nota = tranformar_nota(notadoaluho)
        print("O aluno {} teve seu conceito {} e nota {}".format(nomedoaluno, notadoaluho, nova_nota))
        adicionar_na_lista(listadenotas, notadoaluho)
        adicionar_na_lista(listadegrades, nova_nota)
        adicionar_na_lista(listadenomes, nomedoaluno)

        i -= 1

    printar_resultado(listadenotas, listadenomes, listadegrades)
