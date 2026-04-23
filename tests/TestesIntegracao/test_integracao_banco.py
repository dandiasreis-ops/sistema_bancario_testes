import unittest

#importa as classes
from source.CodigoBase.sistema_bancario_base import (
    ContaCorrente,
    PessoaFisica,
    Deposito,
    Saque
)

class TestIntegracao(unittest.TestCase):

    def setUp(self):
        self.cliente = PessoaFisica("Teste", "123", "01-01-2000", "SP")
        self.conta = ContaCorrente(self.cliente, 1)
        self.cliente.adicionar_conta(self.conta)

    #TESTE 2.1 - Depósito + Histórico
    def test_deposito_registra_historico(self):
        deposito = Deposito(100)

        self.cliente.realizar_transacao(self.conta, deposito)

        self.assertEqual(self.conta.saldo, 100)
        self.assertEqual(len(self.conta.historico.transacoes), 1)
        self.assertEqual(
            self.conta.historico.transacoes[0]["tipo"],
            "Deposito"
        )

    #TESTE 2.2 - Saque + Histórico
    def test_saque_registra_historico(self):
        deposito = Deposito(200)
        self.cliente.realizar_transacao(self.conta, deposito)

        saque = Saque(100)
        self.cliente.realizar_transacao(self.conta, saque)

        self.assertEqual(self.conta.saldo, 100)
        self.assertEqual(len(self.conta.historico.transacoes), 2)
        self.assertEqual(
            self.conta.historico.transacoes[1]["tipo"],
            "Saque"
        )

if __name__ == "__main__":
    unittest.main()

'''
Foram realizados testes de integração envolvendo múltiplas classes do sistema:
- Cliente
- ContaCorrente
- Deposito
- Saque
- Historico

Resultados:
As operações de depósito e saque foram executadas corretamente.
As transações foram registradas no histórico da conta.
O saldo foi atualizado conforme esperado.
'''