'''
    Determinar e mayor de tres numeros ingresados por el teclado
'''
def intercambiar_valores(numero1, numero2):
    return numero2, numero1

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

# Ordenar los números
if numero1 > numero2:
    numero1, numero2 = intercambiar_valores(numero1,numero2)


if numero2 > numero3:
    numero2, numero3 = intercambiar_valores(numero2, numero3)

if numero1 > numero2:
    numero1, numero2 = intercambiar_valores(numero1, numero2)

print(f"Numeros ordenados: {numero1}, {numero2}, {numero3}")
