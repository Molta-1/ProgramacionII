from BoletoAvion.BoletoAvion import BoletoAvion
from BoletoAvion.AlimentoExtra import AlimentoExtra

class BoletoEjecutivo(BoletoAvion):
    def __init__(self, valorBoleto, impuestoSalida, horaSalida, horaLlegada, cliente, ciudad):
        super().__init__(valorBoleto, impuestoSalida, horaSalida, horaLlegada, cliente, ciudad)
        self.alimentos = []

    def totalAlimento(self):
        return sum(a.precio for a in self.alimentos)

    def precioPagar(self):
        return super().precioPagar() + self.totalAlimento()


