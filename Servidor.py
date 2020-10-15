from socket import error
import socket, multiprocessing
   
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
            proceso = multiprocessing.Process(target= self.leer_archivo, args=())
            proceso.daemon = True
            proceso.start()
            print('Nuevo proceso inciado %r', proceso)
            
    def leer_archivo(self):
        # Crear archivo  
        file = open("recibido.png", "wb")
        
        while True:
            try:
                # Recibir datos del cliente.
                archivo =self.conn.recv(1024)
            except error:
                print("Error de lectura.")
                break
            else:
                if archivo:
                    # Compatibilidad con Python 3.
                    if isinstance(archivo, bytes):
                        end = archivo[0] == 1
                    else:
                        end = archivo == chr(1)
                    if not end:
                        # Almacenar datos.
                        file.write(archivo)
                    else:
                        break
        
        print("El archivo se ha recibido correctamente.")
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