# Sistema Bancário em Python
Sistema bancário simples em Python, desenvolvido para fins acadêmicos.

## Funcionalidades
- Criação de cliente
- Criação de conta corrente
- Depósito
- Saque
- Controle de saldo
- Histórico de transações

## Testes Implementados
- Testes Unitários
- Testes de Integração
- Testes Funcionais

## Estrutura do Projeto
source/
CodigoBase/
sistema_bancario_base.py

tests/
TestesUnitarios/test_unitarios_banco.py
TestesIntegracao/test_integracao_banco.py
TestesFuncionais/test_funcionais_banco.py

## Como executar
Para rodar o sistema:
```bash
python source/CodigoBase/sistema_bancario_base.py
python -m unittest discover -s tests
