from BoletoAvion.BoletoAvion import BoletoAvion
from Cliente.Cliente import Cliente
from BoletoAvion.BoletoEjectutivo import BoletoEjecutivo
from BoletoAvion.BoletoClienteFrecuente import BoletoClienteFrecuente
from BoletoAvion.Ciudad import Ciudad
from BoletoAvion.AlimentoExtra import AlimentoExtra


cliente1 = Cliente("Pancho Cruz", "Calle 5, San José", "8888-9999")
ciudad_origen = Ciudad("San José", "08:00 AM")
ciudad_destino = Ciudad("Cancún", "11:30 AM")
ciudades = [ciudad_origen, ciudad_destino]
# Se crea al cliente


boleto_ejecutivo = BoletoEjecutivo(
    valorBoleto=500.0,
    impuestoSalida=40.0,
    horaSalida="08:00 AM",
    horaLlegada="11:30 AM",
    cliente=cliente1,
    ciudad=ciudades
)
# Se crea un boleto ejecutivo

snack1 = AlimentoExtra("A1", "Copa de Vino Premium", 12.5)
snack2 = AlimentoExtra("A2", "Tabla de Quesos", 15.0)
# Se crean los alimentos extra

boleto_ejecutivo.alimentos.append(snack1)
boleto_ejecutivo.alimentos.append(snack2)


print(f"Pasajero: {boleto_ejecutivo.cliente.nombre}")
print(f"Precio Base + Impuestos: ${boleto_ejecutivo.valorBoleto + boleto_ejecutivo.impuestoSalida}")
print(f"Total Alimentos Extras: ${boleto_ejecutivo.totalAlimento()}")
print(f"Monto Total: ${boleto_ejecutivo.PrecioPagar()}\n")
# Se verifica que el boleto ejecutivo haya cargado correctamente

boleto_frecuente = BoletoClienteFrecuente(
    valorBoleto=500.0,
    impuestoSalida=40.0,
    horaSalida="08:00 AM",
    horaLlegada="11:30 AM",
    cliente=cliente1,
    ciudad=ciudades,
    descuento=50.0
)

print(f"Pasajero: {boleto_frecuente.cliente.nombre}")
print(f"Precio Base mas Impuestos Aplicados: ${boleto_frecuente.valorBoleto + boleto_frecuente.impuestoSalida}")
print(f"Descuento Aplicado: -${boleto_frecuente._descuento}")
print(f"Monto Total: (Cliente Frecuente): ${boleto_frecuente.PrecioPagar()}\n")

# Se verifica que el boleto de cliente frecuente haya cargado correctamente
