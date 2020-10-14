from logging import shutdown
import socket
import sys

class Cliente(object):
    def __init__(self, data, hostname, port):
        self.data = data
        self.hostname = hostname
        self.port = port 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def iniciar_con(self):
        # Conectar cliente con el servidor
        server_address = (self.hostname, self.port)
        print('Iniciando conexion con {} puerto {}'.format(*server_address))
        self.sock.connect(server_address)

        
    def enviar_txt(self):
        # Enviar entrada por consola 
        print('Enviando {!r}'.format(self.data))
        self.sock.sendall(self.data.encode())


    def enviar_datos(self):
        # Enviar un archivo de cualquier tipo
        while True:
            file = open(self.data, 'rb')
            contenido = file.read(1024)
            while contenido:
                self.sock.send(contenido)
                contenido = file.read(1024)   
            break   
        try: 
            self.sock(chr(1))
        except TypeError:
            self.sock.send(bytes(chr(1), 'utf-8'))
        finally:
            print('Se envio 1 como confirmacion de envio completo del archivo')
                           
    def verificar_envio(self):
        """
        Verificacion y envio de datos
        Se recive un 1 para confirmar el envio completo
        Se espera 0 para confirmar un error por parte del servidor
        """   
        cantidad_recivida = 0
        cantidad_esperada = 1
        while cantidad_recivida < cantidad_esperada:
            data = self.sock.recv(16)
            cantidad_esperada += len(data)
            print('Recivido {!r}'.format(data))
    
    def cerrar_conexion(self):
        # Cerrar conexion
        print('Conexion terminada')
        self.sock.close()


if __name__ == "__main__":
    data = 'Prueba.png'
    c = Cliente(data, hostname = 'localhost', port = 10000)
    c.iniciar_con()
    c.enviar_datos()
    c.verificar_envio()
    c.cerrar_conexion()
