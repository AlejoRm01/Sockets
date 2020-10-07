class Buckets:
    def __init__(self, id, path):
        self._id = id
        self._path = path
    
    def get_id(self):
        return self._id
    
    def get_path(self):
        return self._path 
    
    def set_id(self,x):
        self._id = x
    
    def set_path(self,x):
        self._path = x