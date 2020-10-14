import socket
import sys

class Cliente(object):
    
    def __init__(self, hostname, port, data):
        self.nombre_data = data
        self.hostname = hostname
        self.port = port 
        self.data = data
        
    def iniciar_con(self):
        # Iniciar servicio
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.hostname, self.port))
    
    def enviar_txt(self):
        self.sock.send(self.nombre_data)
    
    def enviar_archivo(self):
        while True:
            file = open(self.data, "rb")
            self.data = file.read(1024)
            
            while self.data:
                # Enviar contenido.
                self.sock.send(self.data)
                self.data = file.read(1024)
            break 
        # Se utiliza el caracter de código 1 para indicar
        # al cliente que ya se ha enviado todo el contenido.
        try:
            self.sock.send(chr(1))
        except TypeError:
            # Compatibilidad con Python 3.
            self.sock.send(bytes(chr(1), "utf-8"))
        
        # Cerrar archivo.
        file.close()
        print("El archivo ha sido enviado correctamente.")
    
    def cerrar_con(self):
        # Cerrar conexión 
        self.sock.close()


if __name__ == "__main__":
    c = Cliente(hostname = 'localhost', port = 6030, data = 'Prueba.png')
    c.iniciar_con()
    c.enviar_archivo()
    c.cerrar_con()
