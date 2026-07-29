class Ciudad:
    def __init__(self, salida_destino, hora_actual):
        self._salida_destino = salida_destino
        self._hora_actual = hora_actual

    @property
    def salida_destino(self):
        return self._salida_destino
    @property
    def hora_actual(self):
        return self._hora_actual
