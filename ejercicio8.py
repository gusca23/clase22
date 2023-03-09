'''
8- En una tienda se efectúa una promoción en la cual se hace un
descuento sobre el valor de la cuenta total, según el color de la
bolilla que el cliente saque al pagar en caja. Si la bolilla es de
color blanco no se hará descuento alguno, si es verde se le hará
un 10% de descuento, si es amarilla un 25%, si es azul un 50% y si
es roja un 100%. Determinar la cantidad final que el cliente
deberá pagar por su compra. Se sabe que sólo hay bolillas de los
colores mencionados.
'''
valor_total_cuenta = int(input('Favor ingrese el monto a pagar: '))
color_bolilla = input('Favor diga el color de la bolilla sacada: ')

if color_bolilla == 'blanco':
    print('Lastimosamente no contamos con descuento')
elif color_bolilla == 'verde':
    precio_con_descuento = int(valor_total_cuenta * 0.9)
    print(f'el precio sin descuento es de: {valor_total_cuenta}gs, cuenta con un descuento del 10% por lo que estaria abonando {precio_con_descuento}gs')
elif color_bolilla == 'amarillo':
    precio_con_descuento = int(valor_total_cuenta * 0.75)
    print(f'el precio sin descuento es de: {valor_total_cuenta}gs, cuenta con un descuento del 25% por lo que estaria abonando {precio_con_descuento}gs')
elif color_bolilla == 'azul':
    precio_con_descuento = int(valor_total_cuenta * 0.5)
    print(f'el precio sin descuento es de: {valor_total_cuenta}gs, cuenta con un descuento del 50% por lo que estaria abonando {precio_con_descuento}gs')
elif color_bolilla == 'rojo':
    print(f'Felicidades tiene un descuento del 100%')
