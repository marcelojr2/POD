import sys
from Contas import ContaCorrente, ContaInvestimento, ContaPoupança

def criar_conta(arquivo):
    try:
        with open(arquivo, 'r') as a:
            linhas = a.readlines()

        limite = None
        taxa_rendimento = None
        tipo_risco = None
        indice_inicio_operacoes = 0

        for index, linha in enumerate(linhas):
            linha = linha.strip()
            if linha.startswith('Nome Completo:'):
                nome_completo = linha.split('Nome Completo:')[1].strip()
            elif linha.startswith('CPF->'):
                cpf = linha.split('CPF->')[1].strip()
            elif linha.startswith('atribuir id da conta->'):
                numero_conta = int(linha.split('atribuir id da conta->')[1].strip())
            elif linha.startswith('atribuir saldoInicial->'):
                saldo_inicial = float(linha.split('atribuir saldoInicial->')[1].strip())
            elif linha.startswith('criar uma->'):
                tipo_conta = linha.split('criar uma->')[1].strip()
                indice_inicio_operacoes = index + 1
            elif linha.startswith('atribuir limiteChequeEspecial->'):
                limite = float(linha.split('atribuir limiteChequeEspecial->')[1].strip())
            elif linha.startswith('atribuir taxaRendimento->'):
                taxa_rendimento = float(linha.split('atribuir taxaRendimento->')[1].strip())
            elif linha.startswith('atribuir tipoRisco->'):
                tipo_risco = linha.split('atribuir tipoRisco->')[1].strip()
                

        if tipo_conta == 'contaCorrente':
            conta = ContaCorrente(numero_conta, nome_completo, cpf, saldo_inicial, limite)
        elif tipo_conta == 'contaPoupanca':
            conta = ContaPoupança(numero_conta, nome_completo, cpf, saldo_inicial, taxa_rendimento)
        elif tipo_conta == 'contaInvestimento':
            conta = ContaInvestimento(numero_conta, nome_completo, cpf, saldo_inicial, tipo_risco)
        else:
            raise ValueError('Tipo de conta inválido: ' + tipo_conta)

        operacoes = linhas[indice_inicio_operacoes:]
        log = []
        saida = []

        for operacao in operacoes:
            partes = operacao.strip().split('->')
            acao = partes[0]
            if acao in ['realizar saque', 'realizar deposito']:
                try:
                    valor = float(partes[1].strip())
                except ValueError:
                    valor = None

                if acao == 'realizar saque':
                    conta.sacar(valor)
                    

                elif acao == 'realizar deposito':
                    conta.depositar(valor)
                    

            elif acao == 'calcular rendimento':
                texto = partes[1].strip()
                partes = texto.split(':')
                dias = int(partes[1].split()[0])
                conta.calcular_rendimento(dias)
                

            elif acao == 'consultar saldo':
                saldo = conta.consultar_saldo()
                

        saida.append('Dados da conta:')
        saida.append(conta.dados())

        with open(arquivo + '.saida', 'w') as file:
            file.write('\n'.join(saida))

        

    except Exception as e:
        with open(arquivo[:-4] + ".log", "w") as log_arquivo:
            log_arquivo.write(str(e))

arquivos = sys.argv[1:]  # Lista de arquivos passada como argumentos na linha de comando
for arquivo in arquivos:
     criar_conta(arquivo)