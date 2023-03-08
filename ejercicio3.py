'''
3- Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base más comisiones.
'''
sueldo_base = int(input('Ingrese su sueldo'))
comision_por_ventas = (sueldo_base * 0.1) * 3
sueldo_mas_comision = sueldo_base + comision_por_ventas

print(f'la comision por sus tres ventas es de {comision_por_ventas}gs y el total a cobrar sera de {sueldo_mas_comision}gs')