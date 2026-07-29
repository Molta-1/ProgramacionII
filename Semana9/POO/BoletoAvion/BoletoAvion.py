# Importación de librerías y clases
from Cliente.Cliente import Cliente
from .Ciudad import Ciudad


class BoletoAvion:
    def __init__(self, valorBoleto, impuestoSalida, horaSalida, horaLlegada, cliente, ciudad):
        self._valorBoleto = valorBoleto
        self._impuestoSalida = impuestoSalida
        self._horaSalida = horaSalida
        self._horaLlegada = horaLlegada
        # Estos son los valores propios de la clase

        self.cliente = cliente
        self.ciudad = ciudad
        # Estas no poseen guión bajo ya que en el diagrama no se solicita

    @property
    def valorBoleto(self):
        return self._valorBoleto
    @property
    def impuestoSalida(self):
        return self._impuestoSalida
    @property
    def horaSalida(self):
        return self._horaSalida
    @property
    def horaLlegada(self):
        return self._horaLlegada

    def PrecioPagar(self):
        return self._valorBoleto + self._impuestoSalida
    # Esta no posee guión bajo ya que en el diagrama no se solicita
