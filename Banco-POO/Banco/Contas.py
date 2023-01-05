class Carteira:
    def __init__(self, investimento):
        self.__investimento = investimento
        self.__listaContas = []

    @property
    def investimento(self):
        return self.__investimento

    @investimento.setter 
    def investimento(self, investimento):
        self.__investimento = investimento
    
    @property
    def listaContas(self):
        return self.__listaContas

    def addConta(self, objetoConta):
        if len(self.__listaContas) == 3:
            print ("Não é possível ter mais de 3 contas")
        else:
            self.__listaContas += [objetoConta]

    '''def contasNegativas():
        listaNegativas = []
        for continha in self.__listaContas:
            if continha.saldo < 0:
                listaNegativas +=[continha]
        if len(listaNegativas) ==0:
            print("Nenhuma conta está negativa nessa carteira!")        
            return []
        else:
            return listaNegativas'''

class Conta:
    def __init__(self, numero, nome, valor):
        self.__numero = numero
        self.__titular = nome
        self.__saldo = valor

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        partesNomes = self.__titular.split(" ")
        tamanho = len(partesNomes)
        return partesNomes[0] + " " + partesNomes [tamanho - 1]  

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo    

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print ("Não foi possível alterar o saldo! ;-;")
        else:
            self.__saldo = saldo

    def sacar(self, valor):
        if (valor > self.__saldo):
            print ("Não foi possível sacar esse valor! ;-;")
        else:
            self.__saldo -= valor

    def depositar(self, valor):
        if (valor < 0):
            print ("Não foi possível realizar o deposito!") 
        else:
            self.__saldo += valor           

    def retornaDados(self):
        return "Número: " + self.numero + "\n" + "Nome do Titular: " + self.titular + "\n" + "Saldo da Conta: " + str(self.saldo) + "\n\n"

class ContaCorrente(Conta):

    contador = 0

    def __init__(self, numero, nome, valor):
        super().__init__(numero, nome, valor)
        self.__limite = 2000
        ContaCorrente.contador += 1

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        if (limite < 0):
            print ("Não foi possível alterar o limite ;-;")
        else:
            self.__limite = limite 

    def saldoTotal(self):
        return self.saldo + self.__limite   

    def sacar(self, valor):
        if (valor > self.saldoTotal()):
            print ("Não foi possível sacar esse valor! ;-;")
        else:
            if (valor <= self.saldo):
                self.saldo -= valor
            else:
                self.limite = (valor - self.saldo)
                self.saldo = 0

    def retornaDados(self):
        return super().retornaDados() + f"Rendimento: {self.limite} \n\n"

class ContaPoupanca(Conta):
    def __init__(self, numero, nome, valor,  rendimento):
        super().__init__(numero, nome, valor)
        self.__rendimento = rendimento

    @property
    def rendimento(self):
        return self.__rendimento

    @rendimento.setter
    def rendimento(self, rendimento):
        if (rendimento < 0):
            print ("Não foi possível alterar a taxa de rendimento ;-;")
        else:
            self.__rendimento = rendimento

    def acaoRendimento(self):
        self.saldo *= self.__rendimento
    
    def retornaDados(self):
        return super().retornaDados() + f"Rendimento: {self.rendimento} \n\n"