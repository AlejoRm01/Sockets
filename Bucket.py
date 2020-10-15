# Esto todavia sirve pa culo
class Bucket(object):
    def __init__(self, id_bucket):
        self.id_bucket= id_bucket
        self.dicc = {}
        
    def get_id(self):
        return self.id_bucket

    def add_contenido(self, id_contenido, nombre_contenido, contenido):
        c =  Contenido(id_contenido, nombre_contenido, contenido)
        self.dicc[id_contenido] = c 
           
    def get_contenido(self, id_contenido):
        return self.dicc[id_contenido].__dict__
    
    def getAll_contenido(self):
        return self.dicc

    def del_contenido(self, id_contenido):
        del self.dicc[id_contenido]

class Contenido:
    def __init__(self, id_contenido, nombre_contenido, contenido):
        self.id_contenido = id_contenido
        self.contenido = contenido
        self.nombre_contenido = nombre_contenido
        
if __name__ == "__main__":
    
    b = Bucket(1)
    b.add_contenido(1, 'Mi mamá me mima.png','Soy el contenido')
    b.add_contenido(2, 'Hola mundo', 'Matenme')
    b.add_contenido(3, 'Hola ', 'No me maten')
    x =  b.getAll_contenido()
    for y in x:
        print(x[y].__dict__)
    b.del_contenido(2)
    for y in x:
        print(x[y].__dict__)