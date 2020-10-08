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




if __name__ == "__main__":
    data = input()
    c = Cliente(data.encode(), hostname = 'localhost', port = 10000)
    c.star()
    c.shutdown()