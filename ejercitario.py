#1- En una tienda se ha establecido la siguiente oferta: por compras menores a 100.000 se hace un descuento de 8%, pero para compras a partir de 100.000 el descuento es de 10%. Se pide ingresar la cantidad y el precio del producto que se compra y determinar cuánto se descontará y cuanto se cobrará.

cantidad_producto = int(input('ingrese la cantidad del producto'))
precio_producto = int(input('ingrese el precio del producto'))
precio_total = cantidad_producto * precio_producto

if precio_total < 100000:
    descuento = precio_total * 0.08
    total_a_pagar = precio_total - descuento
    print(f'Su descuento es de {descuento} gs.')
    print(f'Debe pagar la cantidad de {total_a_pagar} gs')
else:
    descuento = precio_total * 0.1
    total_a_pagar = precio_total - descuento
    print(f'Su descuento es de {descuento} gs.')
    print(f'Debe pagar la cantidad de {total_a_pagar} gs')

#2- Una empresa quiere hacer una compra de varias piezas de la misma clase en una fábrica de  refacciones. La empresa dependiendo del monto total de la compra decidirá qué hacer para pagar al fabricante. 

# Si el monto total de la compra excede de 500000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante. 

# Si el monto total de la compra no excede de 500000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.