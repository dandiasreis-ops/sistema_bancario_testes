import unittest

#importa as classes
from source.CodigoBase.sistema_bancario_base import (
    PessoaFisica,
    ContaCorrente,
    Deposito,
    Saque
)

class TestFuncional(unittest.TestCase):

    #TESTE 3.1 - Fluxo completo
    def test_fluxo_completo(self):
        cliente = PessoaFisica("Daniel", "123", "01-01-2000", "SP")
        conta = ContaCorrente(cliente, 1)
        cliente.adicionar_conta(conta)

        #Depósito
        cliente.realizar_transacao(conta, Deposito(1000))

        #Saque
        cliente.realizar_transacao(conta, Saque(200))

        #Verificações finais
        self.assertEqual(conta.saldo, 800)
        self.assertEqual(len(conta.historico.transacoes), 2)

    #TESTE 3.2 - Limite de saque
    def test_limite_saques(self):
        cliente = PessoaFisica("Daniel", "123", "01-01-2000", "SP")
        conta = ContaCorrente(cliente, 1)
        cliente.adicionar_conta(conta)

        cliente.realizar_transacao(conta, Deposito(1000))

        #3 saques válidos
        for _ in range(3):
            cliente.realizar_transacao(conta, Saque(100))

        #4º saque (deve falhar)
        cliente.realizar_transacao(conta, Saque(100))

        #Só 3 saques registrados
        saques = [t for t in conta.historico.transacoes if t["tipo"] == "Saque"]

        self.assertEqual(len(saques), 3)

if __name__ == "__main__":
    unittest.main()

'''
Foram realizados testes funcionais simulando o uso completo do sistema bancário:
- Fluxo completo de operações (depósito + saque)
- Verificação de regra de limite de saques

Resultados:
O sistema executou corretamente todas as operações.
O saldo final foi calculado corretamente.
O histórico registrou corretamente todas as transações.
A regra de limite de saques foi respeitada.
'''