class Computador():
    
    def __init__(self, disponible=None, nombre_usuario=None, referencia=None, tamano_ram=None, precio_hora=None, marca=None):
        self._disponible = disponible
        self._nombre_usuario = nombre_usuario
        self._referencia = referencia
        self._tamano_ram = tamano_ram
        self._precio_hora = precio_hora
        self._marca = marca

    def get_disponible(self):
        return self._disponible

    def set_disponible(self, value):
        self._disponible = value

    def get_nombre_usuario(self):
        return self._nombre_usuario

    def set_nombre_usuario(self, value):
        self._nombre_usuario = value

    def get_referencia(self):
        return self._referencia

    def set_referencia(self, value):
        self._referencia = value

    def get_tamano_ram(self):
        return self._tamano_ram

    def set_tamano_ram(self, value):
        self._tamano_ram = value
        
    def get_precio_hora(self):
        return self._precio_hora
    
    def set_precio_hora(self, precio_hora):
        self._precio_hora = precio_hora
    
    def get_marca(self):
        return self._marca
    def set_marca(self, marca):
        self._marca = marca
