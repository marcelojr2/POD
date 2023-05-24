Nosso app é um programa em que permite criar contas bancárias e executar operações nelas através de um arquivo de entrada.

Para criar uma conta bancária, deve ser inserido um arquivo.txt cujo tenha informações como nome, cpf, número da conta e saldo inicial, com o formato seguindo as seguintes regras(sem as aspas):

Nome Completo: 'nome completo'

CPF-> 'CPF'

atribuir id da conta-> 'número da conta'

atribuir saldoInicial-> 'saldo inicial'

Para de fato criar a conta você deve digitar:

criar uma-> 'tipo de conta'

Para a conta corrente, use contaCorrente.
Para a conta poupança, use contaPoupanca.
Para a conta de investimento, use contaInvestimento.

Cada conta tem seu atributo específico.

Na conta corrente:
atribuir limiteChequeEspecial-> 'limite'

Na conta poupança:
 atribuir taxaRendimento-> 'taxa'

Na conta investimento:
atribuir tipoRisco-> [tipo de risco].

Após a linha que indica o tipo de conta, as linhas seguintes representam as operações a serem executadas na conta bancaria. Cada linha deve começar com uma ação, seguida de -> e o valor (quando necessário).

As ações são:
realizar saque-> 'valor'
realizar deposito-> 'valor'
calcular rendimento-> dias: 'número de dias'
consultar saldo:

Após todas as operações, o arquivo .txt deve ser salvo.

Na linha de comando escreva python app.py 'nome dos arquivos'

Ex:
python app.py a.txt b.txt

O programa irá ler o arquivo de entrada, criar a conta bancária, executar as operações especificadas e gerar um arquivo de saída com os resultados(que infelizmente não está completo devido falhas no código na hora da escrita para esse arquivo de saída, porém há informações a serem printadas no terminal).

