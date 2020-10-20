import socket, pickle, struct

class Cliente():
    
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port 
        self.dicc = {}
         
    def iniciar_conexion(self):
        # Iniciar servicio
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.hostname, self.port))
        
    def leer_archivo(self, path):
        file = open(path, 'rb')
        self.dicc['Archivo'] = file.read()
        file.read()
        file.close()
    
    def enviar_archivo(self):
        # Enviar datos al servidor
        x = pickle.dumps(self.dicc)
        length = len(x)
        self.sock.sendall(struct.pack('!I', length))
        self.sock.sendall(x)
        respuesta = self.sock.recv(16)
        print(respuesta)
    
    def recibir_archivo(self):   
        # Recibir datos del servidor.
        lengthbuf = self.recvall(4)
        length, = struct.unpack('!I', lengthbuf)
        datos = self.recvall(length)    
        print(datos)
    
    def recvall (self, count): 
        buf = b'' 
        while count: 
            newbuf = self.sock.recv (count) 
            if not  newbuf: return None 
            buf += newbuf 
            count -= len (newbuf) 
        return buf
    
    def cerrar_conexion(self):
        self.sock.close()
                
if __name__ == "__main__":
    c = Cliente(hostname = 'localhost', port = 6030)
    c.iniciar_conexion()
    c.leer_archivo('Prueba.png')
    c.enviar_archivo()
    c.cerrar_conexion()