import socket
import sys

class Servidor:
    def __init__(self):
        # Crear socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    def conexion(self):
        

        # Enlazando el puerto del socket
        server_address = ('localhost', 10000)
        print('starting up on {} port {}'.format(*server_address))
        self.sock.bind(server_address)

        # Escuchando las conexiones entrantes
        self.sock.listen(1)

        while True:
            # Esperar por la conexion
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            
            print('connection from', client_address)

            #Recibo los datos en pequeños fragmentos y vuelvo a transmitirlos 
            while True:
                data = connection.recv(16)
                print('received {!r}'.format(data))
                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print('no data from', client_address)
                    break
    
    def terminar_conexion(self):
        # Cerrar conexion
        print('Conexion terminada')
        self.sock.close()
 

          

if __name__ == "__main__":
    Servidor.conexion(self = None)