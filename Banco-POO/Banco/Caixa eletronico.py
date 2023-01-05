from Contas import *
from Clientes import *
import os

if __name__ == "__main__":
    listaClientes = []
    listaCarteiras = []
    while True:
        print ("Bem-vindo ao Bank POOdle\n") #Aqui inicia o programa.
        print("(1) Cadastrar um novo cliente.")
        print("(2) Pesquisar por um cliente existente.")
        print("(3) Sair do programa. ;-;\n")
        opcao1 = int(input("Informe a opção desejada: "))
        if opcao1 == 1:
            while True:
                pessoa = input("O titular é uma pessoa física (F) ou jurídica (J): ").upper()
                if pessoa == "F":
                    nome = input("Informe seu nome: ")
                    dn = input("Informe sua data de nascimento: DD/MM/AA ")
                    endereco = input("Informe seu endereço: ")
                    cpf = input("Digite seu CPF: ")
                    pf = PessoaFisica(nome, dn, endereco, cpf) #Variável para adicionar os dados do usuário.
                    pf.maiorLegal(dn) 
                    if pf.maiorLegal(dn) == False: #Identificar se o usuário é maior ou menor de idade.
                        print (pf.maiorLegal(dn))
                        print("O usuário é menor de idade,volte quando tiver + de 18 anos!")
                        exit()
                    else:
                        print (pf.maiorLegal(dn))
                        print ("O usuário é maior de idade, pode continuar.")
                        pass
                    listaClientes += [pf]
                    break
                elif pessoa == "J":
                    nome = input("Informe seu nome: ")
                    dn = input("Informe sua data de nascimento: DD/MM/AA ")
                    endereco = input("Informe seu endereço: ")
                    cnpj = input("Digite o CNPJ do titular: ")
                    pj = PessoaJuridica(nome, dn, endereco, cnpj) #Variável para adicionar os dados do usuário.
                    nome = pj.tipoSociedade() #Identificar o nome do usuário para usar no "TipoSociedade".
                    listaClientes += [pj]
                    break
                else:
                    print("Comando inválido, tente outra vez.")
            print(nome + " cadastrado com sucesso!!")
        elif opcao1 == 2:
            pessoa = input("O titular é uma pessoa física (F) ou jurídica (J): ").upper()
            if pessoa == "F":
                cpf = input("Qual o CPF do titular?\n")
                for clientizinho in listaClientes:
                    if clientizinho.cod == 1:
                        if clientizinho.cpf == cpf:
                            print( "Cliente encontrado!\n")
                            print (clientizinho.retornaDadosCliente()) #Retornando os dados do cliente.
                            opcao2 = input("Deseja adicionar uma nova carteira? (s) (n) \n")
                            if opcao2 == "s":
                                inv = input("Qual o tipo de investimento? \n ")
                                car = Carteira(inv)
                                clientizinho.addCarteira(car) #Adicionando os dados na carteira.
                                resposta = input("Deseja cadastrar uma conta? (s) (n) \n")
                                if resposta == "s":
                                    repetir = "s"
                                    while repetir == "s":
                                        num = input("Informe o número da conta: ")
                                        tit = input("Informe o nome do titular: ")
                                        sld = float(input("Qual o valor do saldo inicial? "))
                                        tip = input("Conta normal (N), Conta Corrente (C) ou Conta Poupança (P)? ").upper()
                                        if tip == "N":
                                            car.addConta(Conta(num, tit, sld)) #Adicionando os dados na conta.
                                        elif tip == "C":
                                            car.addConta(ContaCorrente(num, tit, sld)) #Adicionando os dados na conta.
                                        elif tip == "P":
                                            ren = float(input("Qual o rendimento mensal? "))
                                            car.addConta(ContaPoupanca(num, tit, sld, ren)) #Adicionando os dados na conta.
                                        else:
                                            print("Comando invalido, tente novamente")
                                        print(f"Cadastro da carteira {inv} realizado com sucesso!\n")
                                        repetir = input("Deseja cadastrar uma nova conta? (s) (n)")
                                    for carteira in clientizinho.listaCarteiras:
                                        print(f"A carteira {carteira.investimento} de {clientizinho.nome} possui essas contas: \n")
                                        for continha in carteira.listaContas:
                                            print(continha.retornaDados()) #Retornando os dados.
                                else:
                                    for carteira in clientizinho.listaCarteiras:
                                        print(f"A carteira {carteira.investimento} de {clientizinho.nome} possui essas contas: \n")
                                        for continha in carteira.listaContas:
                                            print(continha.retornaDados())
                            else:
                                for carteira in clientizinho.listaCarteiras:
                                    print(f"A carteira {carteira.investimento} de {clientizinho.nome} possui essas contas: \n")
                                    for continha in carteira.listaContas:
                                        print(continha.retornaDados())
                else:
                    print("Cliente não encontrado, tente novamente.")     

            elif pessoa == "J":
                cnpj = input("Qual o CNPJ do titular?\n")
                for clientizinho in listaClientes:        
                    if clientizinho.cod == 2:
                        if clientizinho.cnpj == cnpj:
                            print( "Cliente encontrado!\n")
                            print (clientizinho.retornaDadosCliente())
                            opcao2 = input("Deseja adicionar uma nova carteira? (s) (n) \n")
                            if opcao2 == "s":
                                inv = input("Qual o tipo de investimento? ")
                                car = Carteira(inv)
                                clientizinho.addCarteira(car)
                                resposta = input("Deseja cadastrar uma conta? (s) (n) \n")
                                if resposta == "s":
                                    repetir = "s"
                                    while repetir == "s":
                                        num = input("Informe o número da conta: ")
                                        tit = input("Informe o nome do titular: ")
                                        sld = float(input("Qual o valor do saldo inicial? \n "))
                                        tip = input("Conta normal (N), Conta Corrente (C) ou Conta Poupança (P)? ").upper()
                                        if tip == "N":
                                            car.addConta(Conta(num, tit, sld))
                                        elif tip == "C":
                                            car.addConta(ContaCorrente(num, tit, sld))
                                        elif tip == "P":
                                            ren = float(input("Qual o rendimento mensal? \n"))
                                            car.addConta(ContaPoupanca(num, tit, sld, ren))
                                        else:
                                            print("Comando invalido, tente novamente")
                                        print(f"Cadastro da carteira {inv} realizado com sucesso!\n")
                                        repetir = input("Deseja cadastrar uma nova conta? (s) (n) \n")
                                    for carteira in clientizinho.listaCarteiras:
                                        print(f"A carteira {carteira.investimento} de {clientizinho.nome} possui essas contas: \n")
                                        for continha in carteira.listaContas:
                                            print(continha.retornaDados())
                                else:
                                    for carteira in clientizinho.listaCarteiras:
                                        print(f"A carteira {carteira.investimento} de {clientizinho.nome} possui essas contas: \n")
                                        for continha in carteira.listaContas:
                                            print(continha.retornaDados())
                            else:
                                for carteira in clientizinho.listaCarteiras:
                                    print(f"A carteira {carteira.investimento} de {clientizinho.nome} possui essas contas: \n")
                                    for continha in carteira.listaContas:
                                        print(continha.retornaDados())
                else:
                    print("Cliente não encontrado, tente novamente.")
            else:
                print("Opção inválida, tente novamente.")
        elif opcao1 == 3:
            break
        else:
            print ("Opção inválida, tente novamente!")
        input () #Dar um tempo pra limpar a tela.
        os.system("cls" if os.name == "nt" else "clear") #Limpar a tela.
    print ("Volte sempre ao Bank POOdle") #Despedida