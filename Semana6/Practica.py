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
print("Longitud del área del cuadrado", str(C1.perimetro()))

# Instacia del cuadrado
cuadrado1 = md.Cuadrado()
cuadrado1.longitud = 8
print("Longitud del cuadrado:", str(cuadrado1.longitud))
# Impresión del valor de la longitud del cuadrado
cuadrado1.calcular_perimetro()
print("Longitud del perímetro del cuadrado", str(cuadrado1.calcular_perimetro()))
# Impresión del valor del perímetro
cuadrado1.calcular_area()
print("Longitud del área del cuadrado", str(cuadrado1.calcular_area()))
# Impresión del área



