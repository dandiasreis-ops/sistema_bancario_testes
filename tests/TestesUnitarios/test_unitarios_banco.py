import unittest

#importa as classes
from source.CodigoBase.sistema_bancario_base import Conta, PessoaFisica

class TestConta(unittest.TestCase):

    def setUp(self):
        #cria um cliente e conta antes de cada teste
        self.cliente = PessoaFisica("Teste", "123", "01-01-2000", "SP")
        self.conta = Conta(self.cliente, 1)

    #TESTE 1.1 - Depósito válido
    def test_deposito_valido(self):
        resultado = self.conta.depositar(100)

        self.assertTrue(resultado)
        self.assertEqual(self.conta.saldo, 100)

    #TESTE 1.2 - Depósito inválido
    def test_deposito_invalido(self):
        resultado = self.conta.depositar(-50)

        self.assertFalse(resultado)
        self.assertEqual(self.conta.saldo, 0)

    #TESTE 1.3 - Saque válido
    def test_saque_valido(self):
        self.conta.depositar(200)
        resultado = self.conta.sacar(100)

        self.assertTrue(resultado)
        self.assertEqual(self.conta.saldo, 100)

    #TESTE 1.4 - Saque inválido
    def test_saque_invalido(self):
        self.conta.depositar(100)
        resultado = self.conta.sacar(200)

        self.assertFalse(resultado)
        self.assertEqual(self.conta.saldo, 100)

if __name__ == "__main__":
    unittest.main()

'''
Foram executados 4 testes unitários:
- Depósito válido
- Depósito inválido
- Saque válido
- Saque inválido

Resultado:
Todos os testes foram executados com sucesso (OK).
'''