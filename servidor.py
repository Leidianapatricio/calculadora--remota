import socket
import threading
import sys
import os

# Estruturação do  Servidor

HOST = '127.0.0.1'
PORT = 40000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = (HOST, PORT)
sock.bind(server)
sock.listen(10)

print('Servidor foi iniciado.')

# Cria um bloqueio no uso da calculadora.
calc = threading.Lock()


def start_cliente(con, client):
  print('Cliente', client)
  
# Aceita a conexão com do cliente
  
  try:
    while True:
        data = con.recv(1024)
        if not data:
            print('Fechando conexão')
            con.close ()
            break
      
     
  except Exception as e:
    print('Erro ao inicializar o servidor', e.args)


def service(con, client):
  # Função que implementa o serviço da calculadora
  # parâmetro con: utilizado para enviar e receber os dados
  # parâmetro client: é o endereço e porta do cliente

  print('Atendendo cliente', client)

  

  operadores = ['+', '-', '*', '/']
  
  
  while True:
    try:
      message = con.recv(1024)
      msg = str(message.decode())
    

      for x in operadores:
        lock.acquire()
        if msg.find(x) > 0:
          op = x
          msg = msg.split(op)
          break
      if op == '+':
        resp = float(msg[0]) + float(msg[1])
       
      elif op == '-':
        resp = float(msg[0]) - float(msg[1])

      elif op == '*':
        resp = float(msg[0]) * float(msg[1])

      elif op == '/':
        resp = float(msg[0]) / float(msg[1])
        if float(msg[1]) != 0:
            resp = float(msg[0]) / float(msg[1])
        else:
            resp = ('Erro: Divisão por zero')
            con.send(str.encode('001'))

      else:
        con.send(str.encode('002'))

      con.send(str(resp.encode()))
      print(client, "solicitação atendida")
    except Exception as e:
      print('Erro nos dados recebidos do cliente', client, ':', e.args)
    lock.acquire()
    
while True:
	try:
		con, client = sock.accept()
	except: break
	threading.Thread(target=start_cliente, args=(con, client)).start()

sock.close()