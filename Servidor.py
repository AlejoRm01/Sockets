import socket
import sys

class Servidor:
    def __init__(self):
        # Crear socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    def iniciar_conexion(self):
        # Enlazando el puerto del socket
        server_address = ('localhost', 10000)
        print('Iniciando conexion en {} puerto {}'.format(*server_address))
        self.sock.bind(server_address)

        # Escuchando las conexiones entrantes
        self.sock.listen(1)

        while True:
            # Esperar por la conexion
            print('Esperando por la conexion')
            connection, client_address = self.sock.accept()
            
            print('Conexion realizada desde', client_address)

            #Recibo los datos en pequeños fragmentos y vuelvo a transmitirlos 
            while True:
                data = connection.recv(16)
                print('recivido {!r}'.format(data))
                if data:
                    print('Enviando confirmacion al cliente')
                    connection.sendall(data)
                else:
                    print('Datos no leidos desde', client_address)
                    break
    
    def terminar_conexion(self):
        # Cerrar conexion
        print('Conexion terminada')
        self.sock.close()
 
if __name__ == "__main__":
    s = Servidor()
    s.iniciar_conexion()
    s.terminar_conexion()