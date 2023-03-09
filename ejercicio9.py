'''
9- Ingresar dos valores en las variables “maximo” y “minimo” y
luego ingresar un valor en la variable “temperatura”. Imprime un
mensaje si el valor de temperatura no está dentro del rango de
marcado por minimo y maximo
'''
maximo = 45
minimo = 5
temperatura = int(input('Favor digite la temperatura actual: '))

if temperatura < minimo or temperatura > maximo:
    print("Ñamano mba'e!")
else:
    print('Tus datos estan dentro del rango minimo y/o maximo')
