import socket
import sys

class Cliente:
    def __init__(self, mensaje):
        self._mensaje = mensaje
       
        # Crear socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def iniciar_conexion(self):
        # Conectar socket con el servidor para que empiece a escuchar 
        server_address = ('localhost', 10000)
        print('connecting to {} port {}'.format(*server_address))
        self.sock.connect(server_address)

        # Enviar datos
        print('sending {!r}'.format(self._mensaje))
        self.sock.sendall(self._mensaje)

        # Esperar respuesta
        amount_received = 0
        amount_expected = len(self._mensaje)
        
        

        while amount_received < amount_expected:
            data = self.sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))
    
    def terminar_conexion(self):
        # Cerrar conexion
        print('Conexion terminada')
        self.sock.close()


mensaje = b'Hola mundo'

if __name__ == "__main__":
    c = Cliente(mensaje)
    c.iniciar_conexion()
    c.terminar_conexion()