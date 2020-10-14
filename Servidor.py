import multiprocessing
from multiprocessing import connection
import socket
   
class Server(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def iniciar_con(self):
        # Inicial servidor
        print("Escuchando")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              
    def lectura_datos(self):
        # Escuchar peticiones en el puerto 10000.
        self.sock.bind((self.hostname, self.port))
        self.sock.listen(0)
        
        file = open("recibido.jpg", "wb")
        conn, addr = self.sock.accept()
        print('Conectado con {!r}'.format(conn, addr))
        while True:
            
            try:
                # Recibir datos del cliente.
                archivo_recivido = conn.recv(1024)
            except TypeError:
                print("Error de lectura.")
                break
            else:
                if archivo_recivido:
                    # Enviar confirmacion del archivo
                    if isinstance(archivo_recivido, bytes):
                        aux = archivo_recivido[0] == 1
                    else:
                        aux = archivo_recivido == chr(1)
                    if not aux:
                        # Almacenar datos. 
                        file.write(archivo_recivido)
                    else:
                        conn.send(b'0')
                        break
            break
        conn.sendall(b'1')            
        print("El archivo se ha recibido correctamente.")
        file.close()
            
    def cerrar_conexion(self):
        # Cerrar conexion
        print('Conexion terminada')
        self.sock.close()

if __name__ == "__main__":
    s = Server("localhost", 10000)
    s.iniciar_con()
    s.lectura_datos()
    s.cerrar_conexion()
