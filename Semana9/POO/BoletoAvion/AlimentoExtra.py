class AlimentoExtra:
    def __init__(self, codigo, descripcion, precio):
        self._codigo = codigo
        self._descripcion = descripcion
        self._precio = precio

    @property
    def codigo(self):
        return self._codigo

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def precio(self):
        return self._precio
