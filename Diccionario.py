class Diccionario:
    def __init__(self, items):
        self._items = items 
        
    def get_dic(self):
        return self._items
    
    def add_dicc(self, x, y):
        self._items[x] = y 
    
    def del_dicc(self, x):
        del self._items[x]
    
        