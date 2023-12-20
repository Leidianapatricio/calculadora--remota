TITULO: CALCULADORA REMOTA

DISCIPLINAS: SO e PROTOCOLOS
Autora: Leidian Patricio
Descrição do problema: A ideia é fazer algo simples e didático para ser usado em ambientes educacionais infantis
como de estimular as crianças para a matemática como o campo da programação na informática. Uma criança iria ficar 
no lado servidor, observando as respostas a cada nova solicitação do cliente(uma outra criança em um outro computador).
Serviços e Funcionalidades:  

Conexão Remota:

A aplicação facilita a conexão remota entre um cliente e um servidor usando sockets TCP/IP.
Operações Básicas de Cálculo:

Os usuários podem realizar operações fundamentais, como adição, subtração, multiplicação e divisão.
Tratamento de Erros:

Implementação de mecanismos de detecção e sinalização de erros, com foco especial na prevenção de divisão por zero.
Comandos Especiais: Além das operações matemáticas, a aplicação suporta comandos especiais, como 'exit', permitindo o 
encerramento da conexão de forma controlada.





COMANDOS:
> Operadores matemáticos ['+' = soma; '-' = subtração; '*' = multiplicação; '/' = divisão]
> 'Exit' = sair do programa

RESPOSTA SOCKET (sucesso):
> Servidor foi iniciado
> Atendendo cliente
> Fechando conexão
> solicitação atendida

REPOSTAS SOCKET (error):
> Erro ao inicializar o servidor
> Erro: Divisão por zero
> Erro nos dados recebidos do cliente

