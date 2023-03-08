'''
7- El IPS quiere clasificar a las personas que se jubilarán en el año
2017. Existen tres tipos de jubilaciones, por edad, por antigüedad
joven y por antigüedad adulta. 

Las personas para la jubilación por
edad deben tener 60 años o más y una antigüedad en su empleo
de menos de 25 años.

Las personas para la jubilación por antigüedad joven deben tener
menos de 60 años y una antigüedad en su empleo de 25 años o
más.

Las personas para antigüedad adulta deben tener 60 años o más
y una antigüedad en su empleo de 25 años o más.
'''
edad_funcionario = int(input('Favor ingrese su edad'))
antiguedad_funcionario = int(input('Favor ingrese su antiguedad'))

if edad_funcionario >= 60 and antiguedad_funcionario <= 25: #jubilacion por edad
    print('podes jubilarte por edad')
elif edad_funcionario < 60 and antiguedad_funcionario >= 25: #jubilacion joven
    print('podes acceder a la jubilacion joven')
elif edad_funcionario >= 60 and antiguedad_funcionario >= 25: #jubilacion adulta
    print('podes acceder a la jubilacion adulta')
else:
    print('todavia no podes jubilarte, animo')