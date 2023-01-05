from datetime import datetime,date #Importar biblioteca
class Cliente:
    def __init__(self, nome, nascimento, endereco):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__endereco = endereco
        self.listaCarteiras = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento
    
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
 
    def addCarteira(self, carteira): #Adicionar os dados da carteira.
        self.listaCarteiras += [carteira]

    def retornaDadosCliente(self): #retornar os dados do cliente.
        carteira = ""
        for carteirinha in self.listaCarteiras:
            carteira = carteira + str(carteirinha.investimento) + ", "
        return (f"Nome: {self.nome}\nCarteiras(s): {carteira}")

class PessoaFisica(Cliente):
    def __init__(self, nome, nascimento, endereco, cpf):
        super().__init__(nome, nascimento, endereco)
        self.__cpf = cpf
        self.__cod = 1

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def cod(self):
        return self.__cod

    @cpf.setter 
    def cpf(self, cpf):
        self.__cpf = cpf

    def maiorLegal(self, data): #Def para ver se o usuário é maior de idade ou não.
        dataAtual = date.today()
        dataAtual = dataAtual.strftime("%d/%m/%Y")
        dataAtual = dataAtual.split("/")
        datat = data.split("/")
        dia = int(datat[0])
        mes = int(datat[1])
        ano = int(datat[2])
        diahj = int(dataAtual[0])
        meshj = int(dataAtual[1])
        anohj = int(dataAtual[2])
        if(anohj - ano) > 18:
            return True
        elif(anohj - ano) == 18:
            if mes < meshj:
                return True
            elif mes == meshj:
                if dia > diahj:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
 
class PessoaJuridica(Cliente):
    def __init__(self, nome, nascimento, endereco, cnpj):
        super().__init__(nome, nascimento, endereco)
        self.__cnpj = cnpj
        self.__cod = 2
   
    @property
    def cod(self):
        return self.__cod
        
    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self,cnpj):
        self.__cnpj = cnpj
 
    def tipoSociedade(self): #Def para saber se a sigla colocada é o nome de uma empresa.
        pj = self.nome
        pessoaJ = pj.split(" ")
        tamanho = len(pessoaJ)
        if pessoaJ[tamanho - 1].upper() == "FC":
            pessoaJ[tamanho - 1] = "Faber Castell"
            pessoa = pessoaJ
            string = " "
            frase = string.join(pessoa)
        elif pessoaJ[tamanho - 1].upper() == "SLA":
            pessoaJ[tamanho - 1] = "Empresa Doida"
            pessoa = pessoaJ
            string = " "
            frase = string.join(pessoa)
        elif pessoaJ[tamanho - 1].upper() == "C/G":
            pessoaJ[tamanho - 1] = "Comunidade Gamer"
            pessoa = pessoaJ
            string = " "
            frase = string.join(pessoa)
            print(frase)
            exit()
        return frase