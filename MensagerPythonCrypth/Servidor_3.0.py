import socket
import threading
import time

host = socket.gethostbyname(socket.gethostname())
port = 80
addr = (host, port)
print('O endereço IP do servidor é: ',host)

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor_socket.bind(addr)
servidor_socket.listen(10)

listadeclientes = set()

def conversa_recebida(convs):
    
    while True:
        
        try:
            mensagem = convs.recv(1024)
            print(mensagem.decode())
            if not mensagem:
                break
            
        except OSError:
            pass
        except ConnectionResetError:
            pass
        
        for cliente in listadeclientes:
            cliente.send(mensagem)

        

    
while True:
    convs, cliente = servidor_socket.accept()
    listadeclientes.add(convs)
    print('Conectado com o cliente: {0}'.format(cliente))
    threading.Thread(target=conversa_recebida,args=(convs,)).start()


