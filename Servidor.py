import multiprocessing
import socket

def handle(connection, address):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("process-%r" % (address,))
    try:
        logger.debug("Conectado %r puerto %r", connection, address)
        while True:
            data = connection.recv(1024)
            if data == b"":
                logger.debug("Socket cerrado remotamente")
                break
            logger.debug("Datos recividos %r", data)
            connection.sendall(data)
            logger.debug("Enviando datos")
    except:
        logger.exception("Problema metodo handle")
    finally:
        logger.debug("Cerrando socket")
        connection.close()

class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("Server")
        self.hostname = hostname
        self.port = port

    def start(self):
        self.logger.debug("Escuchando")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        while True:
            conn, address = self.socket.accept()
            self.logger.debug("Conexión hecha")
            process = multiprocessing.Process(target=handle, args=(conn, address))
            process.daemon = True
            process.start()
            self.logger.debug("Iniciando proceso %r", process)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("localhost", 10000)
    try:
        logging.info("Escuchando")
        server.start()
    except:
        logging.exception("Excepcion inesperada")
    finally:
        logging.info("Parando proceso")
        for process in multiprocessing.active_children():
            logging.info("Parando proceso %r", process)
            process.terminate()
            process.join()
    logging.info("Todo listo")