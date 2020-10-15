import socket, pickle, struct

class Cliente():
    
    def __init__(self, hostname, port, dicc):
        self.hostname = hostname
        self.port = port 
        self.dicc = dicc
        
    def iniciar_con(self):
        # Iniciar servicio
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.hostname, self.port))
    
    def enviar_archivo(self):
        # Enviar informacion de los datos
        length = len(self.dicc)
        self.sock.sendall(struct.pack('!I', length))
        self.sock.sendall(self.dicc)
        print('El archivo ha sido enviado correctamente.')
    
    def cerrar_con(self):
        # Cerrar conexión 
        self.sock.close()

# Gestion cliente

def organizar_dicc():  
    # Organizar el dicc 
    print('Ingrese nombre del archivo con su extencion')
    nombre_archivo = 'Prueba.png'
    print('Ingrese el paht del archivo')
    path_archivo = 'Prueba.png'
    file = open(path_archivo, 'rb') 
    contenido = file.read()
    # Encapsular los datos para enviar solo 1 trama con estos
    dicc = {'nombre_archivo': nombre_archivo,
                    'contenido': contenido}
    dicc_listo = pickle.dumps(dicc)

    file.close()
    return dicc_listo
    
        

if __name__ == "__main__":
    dicc = organizar_dicc()
    c = Cliente(hostname = 'localhost', port = 6030, dicc = dicc)
    c.iniciar_con()
    c.enviar_archivo()
    c.cerrar_con()