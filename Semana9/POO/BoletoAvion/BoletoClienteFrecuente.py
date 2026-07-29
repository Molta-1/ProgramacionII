from BoletoAvion.BoletoAvion import BoletoAvion

class BoletoClienteFrecuente(BoletoAvion):
    def __init__(self, valorBoleto, impuestoSalida, horaSalida, horaLlegada, cliente, ciudad, descuento):
        super().__init__(valorBoleto, impuestoSalida, horaSalida, horaLlegada, cliente, ciudad)
        '''
        Esto es lo que se llamada de "BoletoAvion", recordemos que estos al ser parámetros obligatorios
        entonces se deben de llamar aquí también
        '''

        self._descuento = descuento

    def precioPagar(self):
        return super().PrecioPagar() - self._descuento