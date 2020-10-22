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
                
    def inter_user(self):
        variable = 1;
        while(int(variable) < 5):
            print('Bienvenido a la central de control servidor-socket. En que le podemos ayudar hoy?''\n'+ '1)Enviar un archivo''\n' +'2)Recibir un archivo''\n' +'3)Ver lista de todos los archivos''\n' +'4)Eliminar un bucket''\n5)Cerrar conexion')
            variable= input()
            if(variable == '1'):
                path = input('Ingrese el path del archivo a enviar')
                self.leer_archivo(path)
                self.enviar_archivo()
            if(variable == '2'):
                print('Aca se recibe un archivo')
            if(variable == '3'):
                print('Aca se listan todos los archivos')
            if(variable == '4'):
                print('Aca se eliminan todos los archivos')
            
            if(int(variable) == 5):
                self.cerrar_conexion()


if __name__ == "__main__":
    c = Cliente(hostname = 'localhost', port = 6030)
    c.iniciar_conexion()
    c.inter_user()
