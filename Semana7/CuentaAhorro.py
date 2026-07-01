class Cuenta_Ahorro:
    def __init__(self, cliente, cuenta, saldo):
        self.__cliente = cliente
        self.__cuenta = cuenta
        self.__saldo = saldo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def cuenta(self):
        return self.__cuenta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    @cliente.setter
    def cliente(self, nombre):
        self.__cliente = nombre

    @cuenta.setter
    def cuenta(self, pin):
        self.__cuenta = pin


    def transferencia(self, monto):
        if monto < 1 :
            print("\nIngrese una cantidad valida")
            return

        if monto > self.__saldo:
            print("\nNo posee fondos suficientes")
            return
        else:
            nuevo_saldo = self.__saldo - monto
            self.__saldo = nuevo_saldo
            print("\nEl saldo es de:", str(nuevo_saldo))
            return

    def deposito(self, plata):
        if plata < 1 :
            print("\nIngrese una cantidad valida")
            return

        nuevo_saldo = plata + self.__saldo
        self.__saldo = nuevo_saldo
        print("\nEl saldo es de:", str(nuevo_saldo))
        return

    def interes(self):
        interes = self.__saldo * 0.05
        nuevo_saldo = interes + self.__saldo
        self.__saldo = nuevo_saldo
        print("\nEl saldo con los interes agregados es de:", str(nuevo_saldo))
        return

    def __str__(self):
        return f"\nEl propietario de la cuenta es: {self.__cliente} \nY el saldo es de: {self.__saldo}"