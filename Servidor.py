from socket import error
import pickle
import socket, multiprocessing, struct
   
class Server():
    
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
    
    def iniciar_con(self):
        # Iniciar servicio 
        print('Escuchando')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.hostname, self.port))
        self.sock.listen(1)
    
    def aceptar_con(self):
        # Aceptar solicitudes 
        while True:
            self.conn, self.addr = self.sock.accept()
            print('contectado con %r ', self.conn)
            # Manejo de procesos mediante el uso de un while y el manejo de un metodo
            proceso = multiprocessing.Process(target= self.leer_dic, args=())
            proceso.daemon = True
            proceso.start()
            print('Nuevo proceso inciado %r', proceso)
            
    def leer_dic(self):
        datos = ''     
        # Recibir datos del cliente.
        lengthbuf = self.recvall(self.conn, 4)
        length, = struct.unpack('!I', lengthbuf)
        datos = self.recvall(self.conn, length)
            
        self.org_datos(datos)
        print("El archivo se ha recibido correctamente.")
    
    def recvall (self, sock, count): 
        buf = b'' 
        while count: 
            newbuf = sock.recv (count) 
            if not  newbuf: return None 
            buf += newbuf 
            count -= len (newbuf) 
        return buf
    
    def org_datos(self, x):
        # Separar datos.
        datos = pickle.loads(x)
        file = open('recivido.png', 'wb')
        file.write(datos['contenido'])        
        file.close()
        
    def cerrar_con(self):
        # Cerrar conexión 
        self.sock.close()

if __name__ == "__main__":
    s = Server( hostname = 'localhost', port = 6030)
    s.iniciar_con()
    s.aceptar_con()
    for proceso in multiprocessing.active_children():
        print('Terminando proceso %r', proceso)
        proceso.terminate()
        proceso.join()
    print('Listo')    