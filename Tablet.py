class Tablet():
    def __init__(self, disponible =None, marca=None, referencia=None, nombre_usuario=None, precio_hora=None, tamano_ram=None):
        self._disponible = disponible
        self._marca = marca
        self._referencia = referencia
        self._nombre_usuario = nombre_usuario
        self._precio_hora = precio_hora
        self._tamano_ram = tamano_ram

    def get_disponible(self):
        return self._disponible

    def set_disponible(self, value):
        self._disponible = value

    def get_marca(self):
        return self._marca

    def set_marca(self, value):
        self._marca = value

    def get_referencia(self):
        return self._referencia

    def set_referencia(self, value):
        self._referencia = value

    def get_nombre_usuario(self):
        return self._nombre_usuario

    def set_nombre_usuario(self, value):
        self._nombre_usuario = value

    def get_precio_hora(self):
        return self._precio

    def set_precio_hora(self, value):
        self._precio_hora = value
    
    def get_tamano_ram(self):
        return self._tamano_ram
    def set_tamano_ram(self, value):
        self._tamano_ram = value
        
    def __str__(self):
        return f"Tablet -- Referencia: {self._referencia}, Marca: {self._marca}, Precio: {self._precio_hora}, Disponible: {self._disponible}"
