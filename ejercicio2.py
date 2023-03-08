'''
2-Una empresa quiere hacer una compra de varias piezas de la misma clase en una fábrica de  refacciones. La empresa dependiendo del monto total de la compra decidirá qué hacer para pagar al fabricante. 
___________________________________________________________
Si el monto total de la compra excede de 500000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante. 
___________________________________________________________
Si el monto total de la compra no excede de 500000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante. 
___________________________________________________________
El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.
___________________________________________________________
'''
presupuesto_del_fabricante = int(input('Ingrese el monto total a cobrar'))

if presupuesto_del_fabricante > 500000:
    inversion_empresa = int(presupuesto_del_fabricante * 0.55)
    prestamo_banco = int(presupuesto_del_fabricante * 0.3)
    credito_al_fabricante = presupuesto_del_fabricante - inversion_empresa + prestamo_banco
    
else:
    inversion_empresa = int(presupuesto_del_fabricante * 0.7)
    prestamo_banco = 0
    credito_al_fabricante = presupuesto_del_fabricante - inversion_empresa


credito_al_fabricante_interes = credito_al_fabricante * 1.2

print(f'La empresa puede pagar {inversion_empresa}gs, pidiendo al banco un prestamo de {prestamo_banco}gs y el resto {credito_al_fabricante}gs lo pagara solicitando un credito al fabricante. Al cual estaria debiendo el total de {credito_al_fabricante_interes}gs con los intereses')