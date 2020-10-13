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
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.hostname, self.port))
            self.socket.listen(5)
            while True:
                # Manejo de multiprocesos
                host, port = self.socket.accept()
                print("Conexión hecha")
                process = multiprocessing.Process(target= self.esperar_recivir_con, args=(host, port))
                process.daemon = True
                process.start()
                print("Iniciando proceso %r", process)

    def esperar_recivir_con(self, host, port):
        # Manejo de entradas y salidas ademas de manejo sobre la conexion con el cliente
        file = open("recibido.png", "wb")
        print("process-%r" % (port,))
        print("Conectado %r puerto %r", host, port)
        while True:
            data = host.recv(1024)
            if data == b"":
                print("Socket cerrado remotamente")
                break
            else:
                if data:
                    if isinstance(data, bytes):
                        respuesta = data[0] == 1
                    else:
                        respuesta = data == chr(1)
                    if not respuesta:
                        file.write(data)
                        print("Datos recividos %r", data)
                        
                            
            file.close()                   
            host.close()
            
    
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("localhost", 10000)
    try:
        logging.info("Escuchando")
        server.iniciar_con()
    except:
        logging.exception("Excepcion inesperada")
    finally:
        logging.info("Parando proceso")
        for process in multiprocessing.active_children():
            logging.info("Parando proceso %r", process)
            process.terminate()
            process.join()
    logging.info("Todo listo")
