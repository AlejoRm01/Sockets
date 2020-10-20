import pickle, socket, multiprocessing, struct
   
class Server():
    
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.dicc = {}
        
    def iniciar_conexion(self):
        # Iniciar servicio 
        print('Escuchando')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.hostname, self.port))
        self.sock.listen(1)
    
    def aceptar_conexion(self):
        # Aceptar solicitudes 
        while True:
            self.conn, self.addr = self.sock.accept()
            print('contectado con %r ', self.conn)
            # Manejo de procesos mediante el uso de un while y el manejo de un metodo
            proceso = multiprocessing.Process(target= self.recibir_archivo, args=())
            proceso.daemon = True
            proceso.start()
            print('Nuevo proceso inciado %r', proceso)
    
    def enviar_archivo(self):
        # Enviar informacion de los datos
        length = len(self.dicc)
        self.sock.sendall(struct.pack('!I', length))
        self.sock.sendall(self.dicc)
            
    def recibir_archivo(self):
        datos = ''     
        try:
            # Recibir datos del cliente.
            lengthbuf = self.recvall(self.conn, 4)
            length, = struct.unpack('!I', lengthbuf)
            datos = self.recvall(self.conn, length)
            self.conn.sendall(b'Servidor: 1')    
            print('Datos recibidos')
            self.organizar_datos(datos)
        except Exception:
            self.conn.sendall(b'Servidor:0')
            
    def recvall (self, sock, count): 
        buf = b'' 
        while count: 
            newbuf = sock.recv (count) 
            if not  newbuf: return None 
            buf += newbuf 
            count -= len (newbuf) 
        return buf
    
    def organizar_datos(self, x):
        datos = pickle.loads(x)
        file = open('recibido.png', 'wb')
        file.write(datos['Archivo'])        
        file.close()
        
    def cerrar_con(self):
        # Cerrar conexión 
        self.sock.close()
    
if __name__ == "__main__":
 # Probar conexion entre cliente y socket  
    s = Server( hostname = 'localhost', port = 6030)
    s.iniciar_conexion()
    s.aceptar_conexion()
    for proceso in multiprocessing.active_children():
        print('Terminando proceso %r', proceso)
        proceso.terminate()
        proceso.join()
    print('Listo')  