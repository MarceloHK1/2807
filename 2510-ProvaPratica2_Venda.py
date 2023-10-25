import matplotlib.pyplot as pit


class Armazem:
    def __init__(self):
        self.produtos = {}
        self.precos = ["_" for _ in range(100)]

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Registrar Venda")
            print("2. Calcular Faturamento")
            print("3. Imprimir Faturamento")
            print("4. Percentuais de Vendas")
            print("5. Gravar Dados em Arquivo")
            print("6. Imprimir Gráfico das 5 Mais Vendidas")
            print("7. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.registrar_venda()
            elif opcao == '2':
                self.calcular_faturamento()
            elif opcao == '3':
                self.imprimir_faturamento()
            elif opcao == '4':
                self.percentuais_vendas()
            elif opcao == '5':
                self.gravar_arquivo()
            elif opcao == '6':
                self.imprimir_grafico()
            elif opcao == '7':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def registrar_venda(self):
        numero_produto = int(input("Digite o número do produto (1-100): "))
        quantidade = int(input("Digite a quantidade vendida: "))
        preco = float(input("Digite o preço do produto: "))

        if 1 <= numero_produto <= 100:
            if numero_produto in self.produtos:
                self.produtos[numero_produto] += quantidade
            else:
                self.produtos[numero_produto] = quantidade
                self.precos[numero_produto] = preco
            print("Venda registrada: Produto: {} = Quantidade: {}".format(numero_produto, quantidade))
        else:
            print("Número inválido!")

    def calcular_faturamento(self):
        i = 0
        faturamento = 0
        while i <= 100:
            if i in self.produtos:
                faturamento += self.produtos[i] * self.precos[i]
            i += 1
        return faturamento

    def imprimir_faturamento(self):
        faturamento = self.calcular_faturamento()
        print("\nFaturamento pro Produto:")
        for numero_produto, quantidade in self.produtos.items():
            if self.precos[numero_produto] != "_":
                preco_individual = self.precos[numero_produto] * quantidade
                print("Produto {}: Quantidade {} = Faturamento {}".format(numero_produto, quantidade, preco_individual))
        print("Faturamento Total: ", faturamento)

    def percentuais_vendas(self):
        faturamento = self.calcular_faturamento()
        print("\nPercentual de vendas por produto:")
        for numero_produto, quantidade in self.produtos.items():
            if self.precos[numero_produto] != "_":
                preco_individual = self.precos[numero_produto] * quantidade
                percentual = (preco_individual / faturamento) * 100
                print(f"Produto {numero_produto}: {percentual: .2f}%")

    def gravar_arquivo(self):
        arquivo = open("dados_vendas.txt", "w")
        for numero_produto, quantidade in self.produtos.items():
            if self.precos[numero_produto] != "_":
                preco_individual = self.precos[numero_produto] * quantidade
                dados = f"Produto {numero_produto}: Quantidade {quantidade} = Preco {preco_individual}\n"
                arquivo.write(dados)
        arquivo.close()
        print("Dados guardados no arquivo 'dados_vendas.txt'")

    def imprimir_grafico(self):
        produtos_ordenados = sorted(self.produtos.items(), reverse=True)
        cinco_mais_vendidos = produtos_ordenados[:5]

        produtos = []
        quantidades = []

        for produto, quantidade in cinco_mais_vendidos:
            produtos.append(produto)
            quantidades.append(quantidade)

        pit.bar(produtos, quantidades)
        pit.xlabel("Produto")
        pit.ylabel("Quantidade Vendida")
        pit.title("Os 5 mais vendidos")
        pit.show()


if __name__ == "__main__":
    armazem = Armazem()
    armazem.menu()
