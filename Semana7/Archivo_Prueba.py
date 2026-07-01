import CuentaAhorro as ca

cuenta1 = ca.Cuenta_Ahorro("Jorge", 0, 10000)
cuenta2 = ca.Cuenta_Ahorro("Pancho", 1, 50000)


cuenta1.cliente = "Jorge Alberto"
print(cuenta1.cliente)
print(cuenta1.cuenta)
print(cuenta1.saldo)

cuenta1.transferencia(5000)

cuenta1.transferencia(0)

cuenta1.deposito(10000)

cuenta1.deposito(0)

cuenta1.interes()

print(cuenta1)
print(cuenta2)