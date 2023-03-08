'''
6- Leer dos números, si son iguales que se multipliquen, si el
primero es mayor que el segundo que se resten y sino que se
sumen.
'''
numero1 = int(input('Ingrese un numero'))
numero2 = int(input('Ingrese otro numero'))

if numero1 == numero2:
    nuevo_numero = numero1 * numero2
    print(nuevo_numero)
elif numero1 > numero2:
    nuevo_numero = numero1 - numero2
    print(nuevo_numero)
else:
    nuevo_numero = numero1 + numero2
    print(nuevo_numero)
