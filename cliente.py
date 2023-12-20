import socket
import sys


HOST = '127.0.0.1'
PORT = 40000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = (HOST, PORT)
sock.connect(server)

# Dicionário de comandos
comandos = {
    '+': '+',
    '-': '-',
    '*': '*',
    '/': '/',
    'exit' : 'exit'
    '001':'Erro Divisão por zero',
    '002': 'Comando Inválido. Tente Novamente!'
    
    }

print('Conexão realizada com sucesso!')

print('Para encerrar use EXIT \n')

print("""

    +-----------------------------+
    |       Calculadora           |
    +-----------------------------+
    | [1] [2] [3] [+]             |
    | [4] [5] [6] [-]             |
    | [7] [8] [9] [*]             |
    | [0] [C] [=] [/]             |
    | [exit]                      |
    +-----------------------------+

    """)
try:
  msg = ""
  while msg != "exit":
    msg = input("Digite a operação desejada: ")
    if msg == '':
      continue
    elif msg == 'exit':
      break
    if msg in comandos:
        
        sock.send(str.encode())
        data = sock.recv(1024)
        if data.decode() == '001':
            print('Erro Divisão por zero')
        print(" Restultado:", data.decode())
    else:
        print("Comando inválido. Tente novamente.")
    
except Exception as e:
  print("Erro nos dados recebidos do cliente ")

sock.close()
