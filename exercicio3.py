class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class AnaslistaSistemas(Pessoa):
    def __init__(self, nome, idade, linguagem):
        super().__init__(nome, idade)
        self.linguagem = linguagem

    def gravar(self):
        with open("analistas.txt", "w") as file:
            file.write("Nome: {}\n".format(self.nome))
            file.write("Idade: {}\n".format(self.idade))
            file.write("Linguagem: {}\n".format(self.linguagem))
            file.write("\n")

    def ler(self):
        with open("analistas.txt", "r") as file:
            for i in file:
                print(i)

    def menu(self):
        while True:
            print("0. Sair")
            print("1. Gravar")
            print("2. Ler")

            opcao = int(input("Digite sua opção: "))

            if opcao == 0:
                break
            elif opcao == 1:
                self.gravar()
            elif opcao == 2:
                self.ler()


if __name__ == "__main__":
    analista = AnaslistaSistemas("Marcelo", 18, "Japones")
    analista.menu()
