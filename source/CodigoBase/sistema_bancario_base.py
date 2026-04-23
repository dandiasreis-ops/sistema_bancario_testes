from datetime import datetime #registrar data e hora de cada transação

#CLASSE HISTÓRICO
class Historico:
    def __init__(self):
        self.transacoes = [] #registrar lista de todas as compras de uma conta

    def adicionar_transacao(self, transacao): #adiciona nova transação no histórico
        self.transacoes.append({ #nome da classe, valor da transação, data
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now()
        })

#INTERFACE TRANSAÇÃO
class Transacao:
    def registrar(self, conta): #metodo abstrato para as subclasses
        raise NotImplementedError

#CLASSE DEPÓSITO - depósito como registro
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor  #valor que será depositado

    def registrar(self, conta):
        #tenta depositar o valor na conta
        if conta.depositar(self.valor): #método depositar da classe conta
            #se o depósito deu certo, salva no histórico
            conta.historico.adicionar_transacao(self)

#CLASSE SAQUE - saque como registro
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor  #valor que será sacado

    def registrar(self, conta):
        #tenta sacar o valor da conta
        if conta.sacar(self.valor): #método sacar da classe conta
            #se o saque deu certo, salva no histórico
            conta.historico.adicionar_transacao(self)

#CLASSE CONTA - ações da conta
class Conta:
    def __init__(self, cliente, numero):
        self.saldo = 0.0 #saldo inicial
        self.numero = numero #número da conta
        self.agencia = "0001" 
        self.cliente = cliente #dono da conta
        self.historico = Historico() #um histórico por conta

    #saque como ação
    def sacar(self, valor):
        #verificar se há saldo suficiente
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False #falha no saque
        
        #se houver, subtrair o valor do saldo
        self.saldo -= valor
        return True  #sucesso no saque
    
     #depósito como ação
    def depositar(self, valor):
        #verificar se o valor é válido
        if valor <= 0:
            print("Valor inválido.")
            return False  #falha no depósito
        
        #se for, adicionar o valor no saldo
        self.saldo += valor
        return True #sucesso no depósito
    
    @classmethod #eu havia esquecido como usar isso...
    def nova_conta(cls, cliente, numero):
        #método de classe para criar uma nova conta
        return cls(cliente, numero)
    
#CLASSE CONTA CORRENTE - características da conta
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero) #chama o construtor da classe Conta

        self.limite = limite #limite extra além do saldo
        
        self.limite_saques = limite_saques #quantidade máxima de saques permitidos

        self.saques_realizados = 0 #contador de saques feitos

    #permissão do saque com base em características da conta
    def sacar(self, valor):
        #verificar se atingiu o limite de saques
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques atingido.")
            return False #falha no saque

        #verificar se o valor ultrapassa saldo + limite
        if valor > (self.saldo + self.limite):
            print("Valor excede limite.")
            return False #falha no saque

        #condições atendidas -> chamar o método sacar da classe pai (Conta)
        if super().sacar(valor):
            self.saques_realizados += 1  #incrementa contador de saques
            return True #sucesso no saque

        return False
    
#CLASSE CLIENTE
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco  #endereço do cliente
        self.contas = []          #lista de contas do cliente

    def realizar_transacao(self, conta, transacao):
        #executar uma transação (depósito ou saque)
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        #adicionar uma conta à lista do cliente
        self.contas.append(conta)

#CLASSE PESSOA FÍSICA
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco) #inicializa atributos da classe Cliente

        self.nome = nome #nome da pessoa

        self.cpf = cpf #CPF da pessoa

        self.data_nascimento = data_nascimento #data de nascimento

#Esse bloco só roda quando o arquivo é executado diretamente
if __name__ == "__main__":
    #EXEMPLO DE USO
    #criar um cliente
    cliente = PessoaFisica("Daniel", "12345678900", "01-01-2000", "São Paulo")

    #criar uma conta corrente para esse cliente
    conta = ContaCorrente(cliente, 1)

    #associar a conta ao cliente
    cliente.adicionar_conta(conta)

    #criar um depósito de 1000
    deposito = Deposito(1000)

    #cliente realiza o depósito
    cliente.realizar_transacao(conta, deposito)

    #criar um saque de 200
    saque = Saque(200)

    #cliente realiza o saque
    cliente.realizar_transacao(conta, saque)

    #mostrar saldo final
    print("Saldo:", conta.saldo)

    #mostrar histórico de transações
    for t in conta.historico.transacoes:
        print(t)