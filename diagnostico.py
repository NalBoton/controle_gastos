class Diagnostico:
    def __init__(self):

        self.nome = ""
        self.saudo = 0
        self.gasto1 = 25
        self.gasto2 = 50
        self.gasto3 = 100
        self.gasto4 = 0
        self.entrada = 0


    def nome2(self):
          self.nome = (input("Digite o seu nome: "))

    def lucro(self):
        self.entrada = int(input("Digite seu salário: "))

    def deposito(self):
        self.saudo = self.entrada

    def despesa1(self):
        self.saudo = self.saudo - self.gasto1
        print(f"despesa de {self.gasto1} apllicada")
        
    def despesa2(self):
            self.saudo = self.saudo - self.gasto2
            print(f"despesa de {self.gasto2} apllicada")

    def despesa3(self):
            self.saudo = self.saudo - self.gasto3
            print(f"despesa de {self.gasto3} apllicada")

    def despesa4(self):
            valor = int(input("Digite o valor da despesa: "))
            self.saudo = self.saudo - valor
            print(f"despesa de {valor} aplicada")

    def mensagem(self):
        return f"{self.nome} tem {self.saudo}"

    def instrucao(self):
            print("\n--- MENU DE OPÇÕES ---")
            print("1 = Aplica o gasto 1 (R$25)")
            print("2 = Aplica o gasto 2 (R$50)")
            print("3 = Aplica o gasto 3 (R$100)")
            print("4 = Insira e desconte o valor que desejar")
            print("5 = Consultar as instruções ")
            print("6 = Ver saldo atual ")
            print("7 = Sair do programa")
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
      "5": p1.instrucao
}


while True:

    escolha = input("Escolha uma opção: ")

    if escolha in opcoes_gastos:
        opcoes_gastos[escolha]()

    elif escolha == "6":
        print(p1.mensagem())

    elif escolha == "7":
        print("Saindo, seu diagnóstico final é: ")
        print(p1.mensagem())
        break

    else:
        print("Opção inválida! Digite um número entre 1 e 7.")