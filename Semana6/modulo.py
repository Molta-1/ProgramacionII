import numpy as np
import math as mt
import pandas as pd

class Circulo:
  def __init__(self, diametro = 0):
      self.__diametro = diametro
  def __str__(self):
      return "Diametro: (%i)" % (self.__diametro)
  @property
  def diametro(self):
      return self.__diametro
  @diametro.setter
  def diametro(self, valor_diametro):
      self.__diametro = valor_diametro
  def perimetro(self):
      return self.__diametro * mt.pi
  def area(self):
      return mt.pi * ((self.__diametro / 2)** 2)



class Cuadrado:
  def __init__(self, longitud = 0):
      self.__longitud = longitud
  def __str__(self):
      return "longitud: (%i)" % (self.__longitud )
  def calcular_perimetro(self):
      return self.__longitud * 4
  def calcular_area(self):
      return self.__longitud * self.__longitud
  @property
  def longitud(self):
      return self.__longitud
  @longitud.setter
  def longitud(self, valor_longitud):
      self.__longitud = valor_longitud


class mi_DF():
    def __init__(self, DF=pd.DataFrame()):
        self.__num_filas = DF.shape[0]
        self.__num_columnas = DF.shape[1]
        self.__DF = DF

    @property
    def num_filas(self):
        return self.__num_filas

    @property
    def num_columnas(self):
        return self.__num_columnas

    @property
    def DF(self):
        return self.__DF

    def maximo(self):
        max = self.DF.iloc[0, 0]
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i, j] > max:
                    max = self.DF.iloc[i, j]
        return max

    def valores(self):
        min = self.DF.iloc[0, 0]
        max = self.DF.iloc[0, 0]
        total_ceros = 0
        total_pares = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i, j] > max:
                    max = self.DF.iloc[i, j]
                if self.DF.iloc[i, j] < min:
                    min = self.DF.iloc[i, j]
                if self.DF.iloc[i, j] == 0:
                    total_ceros = total_ceros + 1
                if self.DF.iloc[i, j] % 2 == 0:
                    total_pares = total_pares + 1
        return {'Maximo': max, 'Minimo': min, 'Total_Ceros': total_ceros, 'Pares': total_pares}

    def estadisticas(self, nc):
        media = np.mean(self.DF.iloc[:, nc])
        mediana = np.median(self.DF.iloc[:, nc])
        deviacion = np.std(self.DF.iloc[:, nc])
        varianza = np.var(self.DF.iloc[:, nc])
        maximo = np.max(self.DF.iloc[:, nc])
        minimo = np.min(self.DF.iloc[:, nc])
        return {'Variable': self.DF.columns.values[nc],
                'Media': media,
                'Mediana': mediana,
                'DesEst': deviacion,
                'Varianza': varianza,
                'Maximo': maximo,
                'Minimo': minimo}
    def divisor3(self):
        divisores = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                valor = self.DF.iloc[i, j]
                if isinstance(valor, (int, float)):
                    if valor % 3 == 0:
                        divisores = divisores + 1
        return divisores
    def corcov (self, nc1, nc2):
        columna1 = self.DF.iloc[:, nc1]
        columna2 = self.DF.iloc[:, nc2]
        covarianza = np.cov(columna1, columna2)
        correlacion = np.corrcoef(columna1, columna2)
        columna1n = self.DF.columns[nc1]
        columna2n = self.DF.columns[nc2]
        return {
                'Columna 1':columna1n,
                "Columna 2":columna2n,
                "Correlación": correlacion,
                "Covarianza": covarianza}


class Tarjeta:
    def __init__(self, cliente, pin, saldo = 10000):
        self.__pin = pin
        self.__cliente = cliente
        self.__saldo = saldo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def pin(self):
        return self.__pin

    @property
    def saldo(self):
        return self.__saldo

    def retiro(self, monto):
        if monto > self.__saldo:
            return print("No posee fondos suficientes")
        else:
            self.__saldo = self.__saldo - monto
            return print("El nuevo fondo es de:", str(self.__saldo))

    def deposito(self, plata):
        self.__saldo = plata + self.__saldo
        return print("El saldo es de:", str(plata))



