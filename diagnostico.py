class Diagnostico:
    def __init__(self):

        self.nome = ""
        self.entrada = 0
        self.saudo = 0.0
        self.gasto1 = 25.00
        self.gasto2 = 50.00
        self.gasto3 = 100.00
        self.gasto4 = 0
        self.historico = []
        


    def nome2(self):
          self.nome = (input("Digite o seu nome: "))

    def lucro(self):
        while True:
            try:
                entrada_usuario = input("Digite seu salário: ").replace(',', '.')
                self.entrada = float(entrada_usuario)
                break
            except ValueError:
                print("Erro! Digite um valor numérico válido para o salário (Ex: 1500 ou 1500,50).")

    def deposito(self):
        self.saudo = self.entrada

        salario_formatado = f"{self.entrada:.2f}".replace('.', ',')
        self.historico.append(f"Salário inicial adicionado: R$ {salario_formatado}")

    def despesa1(self):
        self.saudo = self.saudo - self.gasto1
        self.historico.append(f"Gasto 1 aplicado: - R$ {self.gasto1}")
        print(f"despesa de R$ {self.gasto1:.2f} aplicada")
        
    def despesa2(self):
        self.saudo = self.saudo - self.gasto2
        self.historico.append(f"Gasto 2 aplicado: - R$ {self.gasto2}")
        print(f"despesa de R$ {self.gasto2:.2f} aplicada")

    def despesa3(self):
        self.saudo = self.saudo - self.gasto3
        self.historico.append(f"Gasto 3 aplicado: - R$ {self.gasto3}")
        print(f"despesa de R$ {self.gasto3:.2f} aplicada")

    def despesa4(self):
            while True:
                try:
                    entrada_usuario = input("Digite o valor da despesa: ").replace(',', '.')
                    valor = float(entrada_usuario)
                    break
                except ValueError:
                    print("Erro! Digite um valor numérico válido para a despesa.")
            
            self.saudo = self.saudo - valor

            valor_formatado = f"{valor:.2f}".replace('.', ',')
            self.historico.append(f"Gasto 4 aplicado: - R$ {valor_formatado}")
            print(f"despesa de R$ {valor_formatado} aplicada")

    def ver_historico(self):
        print("\n--- HISTÓRICO DE TRANSAÇÕES ---")
        if not self.historico:
            print("Nenhuma movimentação registrada.")
        else:
            for item in self.historico:
                print(f"• {item}")
        print("-------------------------------")

    def mensagem(self):
        saldo_formatado = f"{self.saudo:.2f}".replace('.', ',')
        return f"{self.nome} tem R$ {saldo_formatado}"

    def instrucao(self):
            print("\n--- MENU DE OPÇÕES ---")
            print("1 = Aplica o gasto 1 (R$25)")
            print("2 = Aplica o gasto 2 (R$50)")
            print("3 = Aplica o gasto 3 (R$100)")
            print("4 = Insira e desconte o valor que desejar")
            print("5 = Consultar as instruções ")
            print("6 = Ver saldo atual ")
            print("7 = Ver histórico")
            print("8 = Sair do programa")
            print("---------------------------------------------")


p1 = Diagnostico()
p1.nome2()
p1.lucro()
p1.deposito()
p1.instrucao()

opcoes_gastos = {
      "1": p1.despesa1,
      "2": p1.despesa2,
      "3": p1.despesa3,
      "4": p1.despesa4,
      "5": p1.instrucao,
      "7": p1.ver_historico
}


while True:

    escolha = input("Escolha uma opção: ")

    if escolha in opcoes_gastos:
        opcoes_gastos[escolha]()

    elif escolha == "6":
        print(p1.mensagem())

    elif escolha == "8":
        print("Saindo, seu diagnóstico final é: ")
        print(p1.mensagem())
        break

    else:
        print("Opção inválida! Digite um número entre 1 e 7.")