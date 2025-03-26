'''
    Determinar e mayor de tres numeros ingresados por el teclado
'''

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

# Ordenar los números
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

if numero2 > numero3:
    numero2, numero3 = numero3, numero2

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print(f"Numeros ordenados: {numero1}, {numero2}, {numero3}")
