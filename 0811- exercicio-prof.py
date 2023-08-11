nota = []
nome = []
x = int(input("Digite a quantidade de alunos: "))

for i in range(x):
    print("Aluno {}.".format(i))
    n = float(input("Digite a nota do aluno: "))
    m = input("Digite o nome do aluno {}: ".format(i))

    nota.append(n)
    nome.append(m)

for i in range(len(nome)):
    if nota[i] >= 9.0:
        print("O aluno {} tem conceito A e nota {}".format(nome[i], nota[i]))
    elif nota[i] >= 8.0:
        print("O aluno {} tem conceito B e nota {}".format(nome[i], nota[i]))
    elif nota[i] >= 7.0:
        print("O aluno {} tem conceito C e nota {}".format(nome[i], nota[i]))
    elif nota[i] >= 5.0:
        print("O aluno {} tem conceito D e nota {}".format(nome[i], nota[i]))
    elif nota[i] >= 3.0:
        print("O aluno {} tem conceito E e nota {}".format(nome[i], nota[i]))
    else:
        print("O aluno {} tem conceito F e nota {}".format(nome[i], nota[i]))

print(nota, '    ', nome)
