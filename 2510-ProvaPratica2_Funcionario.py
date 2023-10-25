class Pagamento:
    def __init__(self):
        self.funcionarios = []
        self.arquivo = open("folha_pag.txt", "a")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Cadastrar Funcionário")
            print("2. Imprimir dados dos Funcionários")
            print("3. Calcular Descontos")
            print("4. Imprimir descontos e salários")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastrar()
            elif opcao == '2':
                self.leitura()
            elif opcao == '3':
                self.calcular_descontos()
            elif opcao == '4':
                self.imprimir_descontos(self.calcular_descontos())
            elif opcao == "5":
                break
            else:
                print("Opção inválida!")

    def cadastrar(self):
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        carga_horaria = float(input("Digite a quantidade de horas trabalhadas: "))

        funcionario = {
            'Nome': nome,
            'Cargo': cargo,
            'Salario': salario,
            'Horas_trabalhadas': carga_horaria,
        }
        self.funcionarios.append(funcionario)

        self.arquivo.write(f"Nome: {funcionario['Nome']}\n")
        self.arquivo.write(f"Cargo: {funcionario['Cargo']}\n")
        self.arquivo.write(f"Salario: {funcionario['Salario']}\n")
        self.arquivo.write(f"Horas_trabalhadas: {funcionario['Horas_trabalhadas']}\n")

        print("Dados guardados no arquivo folha_pag.txt")

    def leitura(self):
        self.arquivo.close()
        arquivo = open("folha_pag.txt", "r")
        dados = arquivo.read()
        print(dados)

    def calcular_descontos(self):
        self.arquivo.close()
        descontos = []

        with open("folha_pag.txt", "r") as arquivo:
            linha = arquivo.readlines()

        for i in range(0, len(linha), 4):
            if i+3 < len(linha):
                nome = linha[i].strip().split(": ")[1]
                salario = float(linha[i + 2].strip().split(": ")[1])

                if salario <= 1500:
                    desconto = 0
                elif 1500 < salario <= 3000:
                    desconto = salario * 0.15
                elif 3000 < salario <= 5000:
                    desconto = salario * 0.2
                else:
                    desconto = salario * 0.27

                descontos.append((nome, salario, desconto))

        return descontos

    def imprimir_descontos(self, descontos):
        discounts = 0
        gross_salary = 0
        net_salary = 0

        for nome, salario, desconto in descontos:
            salario_bruto = salario
            salario_liquido = salario - desconto

            print("Funcionário: {}".format(nome))
            print("Salário Bruto: {:.2f}".format(salario_bruto))
            print("Desconto: {:.2f}".format(desconto))
            print("Salário Líquido: {:.2f}\n".format(salario_liquido))

            discounts += desconto
            gross_salary += salario_bruto
            net_salary += salario_liquido

        print("Total dos discontos: {:.2f}".format(discounts))
        print("Total do salário bruto: {:.2f}".format(gross_salary))
        print("Total do salário líquido: {:.2f}".format(net_salary))


if __name__ == "__main__":
    folha_pagamento = Pagamento()
    folha_pagamento.menu()
