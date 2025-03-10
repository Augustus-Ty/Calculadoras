import math
#Codificado por Augusto Zeballos (Ty)
# Entrada de datos
datos = list(map(float, input("Ingrese los valores del vector separados por espacio: ").split()))
Porcentaje = int(input("Ingrese el porcentaje que desea obtener (sin %): "))
k = int(input("Dentro de cuantas desviaciones quiere que se encuentren los datos (1-3): "))
# Calculo del tamaño de la muestra
contador = len(datos)
# Calculo del promedio
prom = sum(datos) / contador
# Calculo de la varianza
sum_varianza = sum((x - prom) ** 2 for x in datos)
vx = sum_varianza / (contador - 1)  # Varianza muestral
# Calculo de la desviación estándar
S = math.sqrt(vx) if vx > 0 else 0  # Evita errores si la varianza es 0
# Calculo del coeficiente de variación
cvx = S / abs(prom) if prom != 0 else 0  # Evita división por cero
# Regla empírica
r1e = prom - (k * S)
r2e = prom + (k * S)
# Regla de Chebyshev 
if Porcentaje < 100:
    k_chebyshev = 1 / math.sqrt(1 - (Porcentaje / 100))
    r1c = prom - (k_chebyshev * S)
    r2c = prom + (k_chebyshev * S)
else:
    r1c = r2c = None  # No tiene sentido calcular para 100%
# Cálculo del coeficiente de asimetría
sum_asimetria = sum((x - prom) ** 3 for x in datos)
asi = sum_asimetria / (contador * (S ** 3)) if S > 0 else 0
# Cálculo del coeficiente de curtosis
sum_curtosis = sum((x - prom) ** 4 for x in datos)
cur = sum_curtosis / (contador * (S ** 4)) if S > 0 else 0
# Salida de resultados
print(f"El promedio es: {prom}")
print(f"La varianza es: {vx}")
print(f"La desviación estándar es: {S}")
print(f"El coeficiente de variación es: {cvx}")
if k in [1, 2, 3]:
    porcentajes_empiricos = {1: 68, 2: 95, 3: 99.7}
    print(f"Aproximadamente un {porcentajes_empiricos[k]}% de las observaciones están dentro del rango [{r1e}; {r2e}]")
if r1c is not None:
    print(f"Al menos un {Porcentaje}% de las observaciones están dentro del rango [{r1c}; {r2c}] según la regla de Chebyshev")
# Interpretación de asimetría
if asi == 0:
    print(f"El coeficiente de asimetría es {asi}, indicando una distribución simétrica")
elif asi > 0:
    print(f"El coeficiente de asimetría es {asi}, indicando una cola hacia la derecha (asimetría positiva)")
else:
    print(f"El coeficiente de asimetría es {asi}, indicando una cola hacia la izquierda (asimetría negativa)")
# Interpretación de curtosis
if cur == 3:
    print(f"El coeficiente de curtosis es {cur}, indicando una distribución mesocúrtica (normal)")
elif cur > 3:
    print(f"El coeficiente de curtosis es {cur}, indicando una distribución leptocúrtica (pico alto)")
else:
    print(f"El coeficiente de curtosis es {cur}, indicando una distribución platicúrtica (pico bajo)")
print("-----------\n","Coded by Ty\n","-----------")