class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def direccion(self):
        return self._direccion

    @property
    def telefono(self):
        return self._telefono

