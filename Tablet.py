class Tablet():
    def __init__(self, disponible =None, marca=None, referencia=None, nombre_usuario=None, precio_hora=None):
        self._disponible = disponible
        self._marca = marca
        self._referencia = referencia
        self._nombre_usuario = nombre_usuario
        self._precio_hora = precio_hora

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
