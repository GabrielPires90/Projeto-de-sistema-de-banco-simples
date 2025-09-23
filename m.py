import datetime as date


class Cliente :
    def __init__(self):
        self.nome = input("Digite seu nome todo: ")
        self.idade = input("Digite sua idade: ")
        self.cpf = input("Digite seu cpf: ")
        self.cheque_especial = int(input("Digite o limite do seu cheque especial: "))
        self.movimentacoes = []
        self.saldo = 0

    def depositar(self, valor, data):
            self.saldo += valor
            self.movimentacoes.append ({"Tipo:":"Deposito" , "Valor:":valor ,"Data:":data})
            print (f"Depósito de R${valor} realizado com sucesso!")
    
    def sacar(self, valor, data):
        if valor <= self.saldo + self.cheque_especial :
            self.saldo -= valor
            self.movimentacoes.append ({"Tipo:":"Saque" , "Valor:":valor ,"Data:":data})
            if self.saldo < 0 :
                    print(f"Saldo insuficiente,foi utilizados R${abs(self.saldo)} de R${self.cheque_especial} de seu cheque especial!")
            else :
                    print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print("Voce nao possui saldo e nem limite em seu cheque especial o suficiente para este valor!")

    def extrato(self):
         print("========EXTRATO========")

         for mov in self.movimentacoes:
            print(f"{sorted.mov['Data:']} - {mov['Tipo:']} de R${mov['Valor:']}")
            if mov["Tipo:"] == "Deposito":
                 self.saldo_parcial += mov['Valor:']
            else:
                 self.saldo_parcial -=  mov['Valor:']
            print(f"\n Saldo parcial do dia:R${self.saldo_parcial}")

    print("=======================")