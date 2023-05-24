from abc import ABC, abstractmethod 

class Moeda:
    def __init__(self, valor): #metodo construtor que vai criar objetos que serao utilizados nos demais metodos.. diferente do metodo normal, nao preciso ficar chamando
        self.valor = valor
    
    def __add__(self,aux): #vai apenas printar e mostrar como ficaria a operacao sem alterar o valor da moeda
        if isinstance(aux, Moeda):
            return Moeda(self.valor + aux.valor)
        elif isinstance(aux, (int, float)):
            return Moeda(self.valor + aux)
        else: 
            print("Esta operacao nao pode ser realizada")

    def __adicionar__(self,aux): #vai alterar o valor da moeda e printar como ela fica atualizada
        if isinstance(aux, Moeda):
            self.valor = self.valor + aux.valor
        elif isinstance(aux, (int, float)):
            self.valor = self.valor + aux
        else:
            print("Esta operacao nao pode ser realizada")
        return self
    
    def __sub__(self, aux): #vai apenas printar e mostrar como ficaria a operacao sem alterar o valor da moeda
        if isinstance(aux, Moeda):
            return Moeda(self.valor - aux.valor)
        elif isinstance(aux, (int, float)):
            return Moeda(self.valor - aux)
        else:
            print("Esta operacao nao pode ser realizada")

    def __subtrair__(self,aux): #vai alterar o valor da moeda e printar como ela fica atualizada
        if isinstance(aux, Moeda):
            self.valor = self.valor - aux.valor
        elif isinstance(aux, (int, float)):
            self.valor = self.valor - aux
        else:
            print("Esta operacao nao pode ser realizada")
        return self
    
    def __MenorQue__(self, aux): #comparacao entre moedas e pa
        if isinstance(aux, Moeda):
            return self.valor < aux.valor
        elif isinstance(aux, (int, float)):
            return self.valor < aux
        else:
            print("Esta operacao nao pode ser realizada")

    def __MenorOuIgual__(self, aux): #comparacao entre moedas e pa
        if isinstance(aux, Moeda):
            return self.valor <= aux.valor
        elif isinstance(aux, (int, float)):
            return self.valor <= aux
        else:
            print("Esta operacao nao pode ser realizada")

    def __igual__(self, aux): #comparacao entre moedas e pa
        if isinstance(aux, Moeda):
            return self.valor == aux.valor
        elif isinstance(aux, (int, float)):
            return self.valor == aux
        else:
            print("Esta operacao nao pode ser realizada")

    def __str__(self):
        return str(self.valor) #exibe o valor da moeda

class TransacaoInvalida(Exception):
    """Exceção base para transações bancárias inválidas"""
class ErroValorNegativo(TransacaoInvalida):
    """Exceção para valores negativos em transações"""    
class ErroSaldoInsuficiente(TransacaoInvalida):
    """Exceção para saques sem saldo suficiente"""
class ErroAcimaDoLimite(TransacaoInvalida):
    """Exceção para saques acima do limite"""
class ErroTaxaInvalida(TransacaoInvalida):
    """Exceção para taxas inválidas na conta poupança"""
class ErroRiscoInvalido(TransacaoInvalida):
    """Exceção para tipo de risco inválido"""

    
class ContaBancaria(ABC):

    qtd_total=0
    qtd_corrente=0
    qtd_poupanca=0
    qtd_investimento=0

    def __init__(self, numero_conta, nome_cliente, cpf, saldo):
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.saldo = saldo
        ContaBancaria.qtd_total += 1

        self.excecao_numero_conta(numero_conta)
        self.excecao_nome_cliente(nome_cliente)
        self.excecao_cpf(cpf)
        self.excecao_saldo(saldo)

 
    def excecao_numero_conta(self, numero_conta): #excecao do numero da conta pra ter 4 numeros 
        if not isinstance(numero_conta, int) or len(str(numero_conta)) != 4:
            raise ValueError("O número da conta deve ser um inteiro de 4 dígitos.")
    
    def excecao_nome_cliente(self, nome_cliente): #excecao do nome do cliente pra ter até 50 caracteres
        if not isinstance(nome_cliente, str) or len(nome_cliente) > 50:
            raise ValueError("O nome do cliente deve ser uma string com no máximo 50 caracteres.")
    
    def excecao_cpf(self, cpf): #excecao do cpf pra ter 11 numeros 
        if not isinstance(cpf, str) or len(cpf) != 11:
            raise ValueError("O CPF deve ser uma string numérica de 11 dígitos.")
        
    def excecao_saldo(self, saldo): #execao do saldo pra ser positivo
        if not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("O saldo deve ser um número positivo.")
 
   
    @abstractmethod
    def depositar(self, valor):
        pass
   
    @abstractmethod
    def sacar(self, valor):
        pass
   
    @abstractmethod
    def consultar_saldo(self):
        pass

    @abstractmethod
    def calcular_rendimento(self):
        pass

    @abstractmethod
    def tipo_conta(self):
        pass

    @abstractmethod
    def dados(self):
        pass

    
class ContaCorrente(ContaBancaria):
   
    def __init__(self, numeroConta, nome, cpf, saldo, limite):
        super().__init__(numeroConta, nome, cpf, saldo)
        self.limite=limite
        self.taxa = 0.01
        ContaBancaria.qtd_corrente += 1
        
    def depositar(self, valor):
        if valor is not None and valor < 0:
            raise ErroValorNegativo("Valor do depósito não pode ser negativo.")
        else:
            if valor is not None:
                self.saldo += valor
                print("Seu depósito foi realizado com sucesso!")
                print("Novo saldo:"+self.saldo)
   
    def sacar(self, valor):
        if valor is not None and valor < 0:
            raise ErroValorNegativo("Valor do saque não pode ser negativo.")
        if self.limite > 0:
            raise ErroAcimaDoLimite("Limite precisa ser menor ou igual a 0")
        if valor is not None and valor <= self.saldo + self.limite:
            print("Saque foi realizado com sucesso!")
            if valor is not None and valor <= self.saldo:
                self.saldo -= valor
            else:
                if valor is not None:
                    self.limite -= (valor - self.saldo)
                    self.saldo = 0
        else:
           raise ErroSaldoInsuficiente("Saldo insuficiente para completar a transação")
        print("Novo saldo:"+self.saldo)

    def calcular_rendimento(self, dias):
        self.dias=dias
        taxa_diaria=self.taxa/30
        rendimento_diario=taxa_diaria*self.saldo
        rendimento=rendimento_diario*dias
        print("Seu rendimento nesse tempo é de:")
        print(rendimento)
        self.saldo+=rendimento #saldo recebe o rendimento de acordo com o numero de dias declarado

    def consultar_saldo(self):
        print(self.saldo)
        return self.saldo
        
    def tipo_conta(self):
        print("Sua conta é uma conta corrente.")

    def dados(self):
        print("Conta:"+self.nome_cliente)
        print(self.numero_conta)
        print(self.cpf)
        print(self.saldo)
        return self.nome_cliente

   
class ContaInvestimento(ContaBancaria):

    def __init__(self, numeroConta, nome, cpf, saldo, tipoDeRisco):
        super().__init__(numeroConta, nome, cpf, saldo)
        self.tipoDeRisco=tipoDeRisco
        ContaBancaria.qtd_investimento += 1
        

    def depositar(self, valor):
        if valor is not None and valor < 0:
            raise ErroValorNegativo("Valor do depósito não pode ser negativo.")
        else:
            if valor is not None:
                self.saldo += valor
                print("Seu depósito foi realizado com sucesso!")
                print("Novo saldo:"+self.saldo)
   
    def sacar(self, valor):
        if valor is not None and valor < 0:
            raise ErroValorNegativo("Valor do saque não pode ser negativo.")
        elif valor is not None and valor > self.saldo:
            raise ErroSaldoInsuficiente("Saldo insuficiente.")
        else:
            if valor is not None:
                self.saldo -= valor
                print("Saque foi realizado com sucesso!")
                print("Novo saldo:"+self.saldo)

    def calcular_rendimento(self,dias):
        if self.tipoDeRisco == "Baixo":
            self.taxa=0.1
        elif self.tipoDeRisco == "Medio":
            self.taxa=0.25
        elif self.tipoDeRisco == "Alto":
            self.taxa=0.5
        else:
           raise ErroRiscoInvalido("Tipo de risco inválido!")
        
        taxa_diaria=self.taxa/30
        rendimento_diario=self.saldo*taxa_diaria
        rendimento=rendimento_diario*dias
        print("Seu rendimento mensal é de:")
        print(rendimento)
        self.saldo+=rendimento #saldo recebe o rendimento de acordo com o numero de dias declarado

    def consultar_saldo(self):
        print(self.saldo)
        return self.saldo
    
    def tipo_conta(self):
        print("Sua conta é uma conta investimento.")

    def dados(self):
        print("Conta:"+self.nome_cliente)
        print(self.numero_conta)
        print(self.cpf)
        print(self.saldo)
        return self.nome_cliente

   
class ContaPoupança(ContaBancaria):
    
    def __init__(self, numeroConta, nome, cpf, saldo, taxa):
        super().__init__(numeroConta, nome, cpf, saldo)
        self.taxa= taxa
        ContaBancaria.qtd_poupanca += 1

    def depositar(self, valor):
        if valor is not None and valor < 0:
            raise ErroValorNegativo("Valor do depósito não pode ser negativo.")
        else:
            if valor is not None:
                self.saldo += valor
                print("Seu depósito foi realizado com sucesso!")
                print("Novo saldo:"+self.saldo)
   
    def sacar(self, valor):
        if valor is not None and valor < 0:
            raise ErroValorNegativo("Valor do saque não pode ser negativo.")
        elif valor is not None and valor > self.saldo:
            raise ErroSaldoInsuficiente("Saldo insuficiente.")
        else:
            if valor is not None:
                self.saldo -= valor
                print("Saque foi realizado com sucesso!")
                print("Novo saldo:"+self.saldo)
        
    def calcular_rendimento(self,dias):
        if self.taxa >= 0 and self.taxa <= 1:
            taxa_diaria=self.taxa/30
            rendimento_diario=self.saldo*taxa_diaria
            rendimento=rendimento_diario*dias
            print("Seu rendimento mensal é de:")
            print(rendimento)
        else:
            raise ErroTaxaInvalida("A taxa precisa ser associada de 0 a 1.")
        self.saldo+=rendimento #saldo recebe o rendimento de acordo com o numero de dias declarado
        
    def consultar_saldo(self):
        print(self.saldo)
        return self.saldo
    
    def tipo_conta(self):
        print("Sua conta é uma conta poupança.")

    def dados(self):
      
        print("Conta:"+self.nome_cliente)
        print(self.numero_conta)
        print(self.cpf)
        print(self.saldo)
        return self.nome_cliente
   
def status_contas():
    
   print("Contas Correntes criadas:", ContaBancaria.qtd_corrente)
   print("Contas de Investimento criadas:", ContaBancaria.qtd_investimento)
   print("Contas Poupança criadas:", ContaBancaria.qtd_poupanca)
   print("Total de contas criadas:", ContaBancaria.qtd_total)

def saque_verboso(objeto, valor):
    print("Os dados da conta são:")
    objeto.dados()
    print()
    objeto.sacar(valor)
    print("Novo saldo:")
    objeto.consultar_saldo()
    




