from logging import shutdown
import socket
import sys

class Cliente(object):
    def __init__(self, data, hostname, port):
        self.data = data
        self.hostname = hostname
        self.port = port 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def star(self):
        # Conectar socket con el servidor para que empiece a escuchar 
        server_address = (self.hostname, self.port)
        print('Iniciando conexion con {} puerto {}'.format(*server_address))
        self.sock.connect(server_address)

        # Enviar datos
        print('Enviando {!r}'.format(self.data))
        self.sock.sendall(self.data)

        # Esperar respuesta
        amount_received = 0
        amount_expected = len(self.data)
        

        while amount_received < amount_expected:
            data = self.sock.recv(16)
            amount_received += len(data)
            print('Recivido {!r}'.format(data))
    
    def shutdown(self):
        # Cerrar conexion
        print('Conexion terminada')
        self.sock.close()

def switcher_bucket(opcion):
    pass

def switcher_envio(opcion):
    if opcion == '1':
        return input()
    if opcion == '2':
        return

def menu(): 
    
    print('Elige una opcion \n1) Opciones envio de datos \n2) Opciones buckets') 
    aux = input()
    if aux == '1':
        print('1) Enviar texto plano \n2) Eliminar archivo')
        aux_a = input()
        return switcher_envio(aux_a)
        
    if aux == '2':
        
        print('1) Crear bucket \n2) Eliminar bucket \n3) Listar buckets \n4) Listar archivos de un bucket')
        aux_a = input()
        switcher_bucket(aux_a)

if __name__ == "__main__":
    data = menu()
    c = Cliente(data.encode('utf-8'), hostname = 'localhost', port = 10000)
    c.star()
    c.shutdown()
    
def bucket_ops(opcion):
    pass