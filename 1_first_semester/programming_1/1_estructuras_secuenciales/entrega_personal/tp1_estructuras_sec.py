 # 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 

print("Hola Mundo!.")
 
# 2) 
# Crear un programa que pida al usuario su nombre 
# Que imprima por pantalla un saludo usando el nombre ingresado. 

nombre = input("Ingrese su nombre")

print(f"Hola {nombre}, es un placer conocerte")

# 3)
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia
# Que imprima por pantalla una oración con los datos ingresados. 

nombre = input("Ingresa tu NOMBRE")
apellido = input("Ingresa tu APELLIDO")
edad = int(input("Ingresa tu EDAD"))
residencia = input("Ingresa tu lugar de RESIDENCIA")

print(f"\nHola {nombre} {apellido}.",
      f"\nTu edad es {edad}.",
      f"\nY tu lugar de residencia es {residencia}."
)

# 4)
# Crear un programa que pida al usuario el radio de un círculo
# Que imprima por pantalla su área y su perímetro.

PI = 3.1416
radio = 0

radio = float(input("Ingrese el radio. "))
area = PI * (radio**2)
perimetro = 2 * PI * radio

print(f"\nEl radio ingresado es {radio}", 
      f"\nTomando pi con un valor de 3.1416",
      f"\nEl PERIMETRO es {perimetro:.4f}",
      f"\nEl AREA es {area:.4f}"
)

# 5)
# Crear un programa que pida al usuario una cantidad de segundos
# Que imprima por pantalla a cuántas horas equivale

segundos = int(input("Ingrese los segundos. "))

horas = segundos / 3600
minutos = segundos / 60

print(f"\nIngresaste {segundos} segundos.",
      f"\nEquivale a {horas:.2f} horas o {minutos:.2f} minutos."
)

# 6)
# Crear un programa que pida al usuario un número
# Que imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese el numero al cual le desea conocer su respetiva tabla de multiplicar. "))

print(f"\n{numero} x 0 = ", numero * 0,
      f"\n{numero} x 1 = ", numero * 1,
      f"\n{numero} x 2 = ", numero * 2,
      f"\n{numero} x 3 = ", numero * 3,
      f"\n{numero} x 4 = ", numero * 4,
      f"\n{numero} x 5 = ", numero * 5,
      f"\n{numero} x 6 = ", numero * 6,
      f"\n{numero} x 7 = ", numero * 7,
      f"\n{numero} x 8 = ", numero * 8,
      f"\n{numero} x 9 = ", numero * 9,
      f"\n{numero} x 10 = ", numero * 10
)

# 7)
# Crear un programa que pida al usuario dos números enteros distintos del 0 
# Que imprima el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_1 = int(input("Ingrese el primer numero ENTERO, diferente a 0. "))
while numero_1 == 0: 
    numero_1 = int(input("Ingrese el primer numero ENTERO, diferente a 0. "))
 
numero_2 = int(input("Ingrese el segundo numero ENTERO, diferente a 0. "))
while numero_2 == 0:
    numero_2 = int(input("Ingrese el segundo numero ENTERO, diferente a 0. "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multi = numero_1 * numero_2
divi = float(numero_1 / numero_2)

print(f"\n{numero_1} + {numero_2} = {suma}",
      f"\n{numero_1} - {numero_2} = {resta}",
      f"\n{numero_1} * {numero_2} = {multi}",
      f"\n{numero_1} / {numero_2} = {divi:.2f}",
)

# 8)
# Crear un programa que pida al usuario su altura y su peso
# Que imprima por pantalla su índice de masa corporal. 
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜(𝑘𝑔) / 𝑎𝑙𝑡𝑢𝑟𝑎(m)**2

altura = float(input("Ingresa tu altura en Metros. "))
peso = float(input("Ingresa tu peso en Kg"))
imc = peso / (altura **2)

print(f"\nCon un peso de {peso} Kilos",
      f"\nY"
      f"\nCon una altura de {altura} Metros",
      f"\nTu IMC es de {imc:.2f}"
)

# 9)
# Crear un programa que pida al usuario una temperatura en grados Celsius
# Que imprima por pantalla su equivalente en grados Fahrenheit. 
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎(𝐶𝑒𝑙𝑠𝑖𝑢𝑠) + 32

celsius = float(input("Ingrese la temperatura actual, en grados Celsius. "))
fahrenheit = (9 /5) * celsius + 32

print(f"{celsius}º Celsius equivalen a {fahrenheit}º Fahrenheit.")

# 10)
# Crear un programa que pida al usuario 3 números
# Que imprima por pantalla el promedio de dichos números.

numero_1 = float(input("Ingrese el PRIMER numero: "))
numero_2 = float(input("Ingrese el SEGUNDO numero: "))
numero_3 = float(input("Ingrese el TERCER numero: "))

promedio = float((numero_1 + numero_2 + numero_3) / 3)

print(f"El promedio de los 3 numeros es: {promedio}")

# ----------