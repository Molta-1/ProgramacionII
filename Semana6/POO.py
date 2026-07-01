import modulo as md
import pandas as pd

df_estudiantes = pd.read_csv("ejemplo_estudiantes.csv", delimiter=';', decimal=',')
df = md.mi_DF(df_estudiantes)
print("Numero de filas", str(df.num_filas))



# Práctica: Parte 1
# Crear instancias(objeto) de círculo
C1 = md.Circulo() # Creación del objeto
print(C1) # Se imprime el atributo por medio del property
C1.diametro = 10 # Ingreso de valor
print(C1.diametro) # Devuelve instancia con valor
C1.perimetro()
print("Longitud del perímetro del círculo", str(C1.perimetro()))
C1.area()
print("El área del círculo es de:", str(C1.area()))



# Práctica: Parte 2
DF_ejemplo = md.mi_DF(df_estudiantes)
DF_ejemplo.divisor3()
print("Números que se dividen entre 3:", str(DF_ejemplo.divisor3()))

DF_ejemplo.corcov(1, 4)
print(DF_ejemplo.corcov(1, 4))



# Práctica: Parte 3
Cliente1 = md.Tarjeta("Sebastian", 0, 10000)
retiro = Cliente1.retiro(5000)
print(retiro)

deposito = Cliente1.deposito(15000)
print(deposito)