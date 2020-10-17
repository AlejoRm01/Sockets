from bucket import Bucket
import pickle, socket, multiprocessing, struct

from bucket import Contenido
   
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
        # Esta parte es una pruba aca se deberia organizar el manejo de archivo idealmente llamando otros metodos
        datos = pickle.loads(x)
        file = open('recibido.png', 'wb')
        file.write(datos['contenido'])        
        file.close()
        
    def cerrar_con(self):
        # Cerrar conexión 
        self.sock.close()

# Gestion de servidor
class gestion_servidor:
    
    def __init__(self):
        self.dicc = {}
        
    def add_bucket(self, id_bucket):
        b = Bucket(id_bucket)
        self.dicc[id_bucket] = b
    
    def get_bucket(self, id_bucket):
        return self.dicc[id_bucket]
    
    def getAll_bucket(self):
        return self.dicc
    
    def del_bucket(self, id_bucket):
        del self.dicc[id_bucket]
    
    def add_contenido(self, id_bucket, id_contenido, nombre_contenido, contenido):
        self.dicc[id_bucket].add_contenido(id_contenido, nombre_contenido, contenido)
    
    def get_contenido(self, id_bucket, id_contenido):
        self.dicc[id_bucket].get_contenido(id_contenido)
    
    def getAll_contenido(self, id_bucket):
        self.dicc[id_bucket].getAll_bucket()
    
    def del_contenido(self, id_bucket, id_contenido):
        self.dicc[id_bucket].del_contenido(id_contenido)
    
if __name__ == "__main__":
    
    g = gestion_servidor()
    g.add_bucket(1)
    g.add_bucket(2)
    g.add_contenido(1, 1, 'Mi mamá me mima.png','Soy el contenido')
    g.add_contenido(1, 2, 'Hola mundo', 'Matenme')
    g.add_contenido(1, 3, 'Hola ', 'No me maten')
    g.add_contenido(2, 1, 'Mi mamá me ama ','Soy el putas')
    g.add_contenido(2, 2, 'Hola mundo HP', 'AHORQUENME')
    g.add_contenido(2, 3, 'Adios', 'Alfredo es gay')   
    contenedor = g.getAll_bucket()
    # Listar informacion todos los buckets y listar informacion que hay en cada uno 
    for x in contenedor:
        print('Contenido del bucket: %r', x)
        aux = contenedor[x].__dict__
        for y in aux['dicc']:
            print(aux['dicc'][y].__dict__)      
    print('3')
    g.del_bucket(1)
    g.del_contenido(2,1)
    print(g.get_bucket(2))
    # Listar contenido de un bucket en especifico    
    print('1')
    contenedor = g.get_bucket(1).__dict__
    print('Informacion de contenedor: %r', contenedor['id_bucket'])
    for x in contenedor['dicc']:
        print(contenedor['dicc'][x].__dict__)
         
        
       
    ''' 
    # Probar conexion entre cliente y socket  
    s = Server( hostname = 'localhost', port = 6030)
    s.iniciar_con()
    s.aceptar_con()
    for proceso in multiprocessing.active_children():
        print('Terminando proceso %r', proceso)
        proceso.terminate()
        proceso.join()
    print('Listo')    
    '''