
# cond 1: Si tiene menos de 18 es menor.
# cond 2: Si tiene entre 18 y 125 es un zombie.
# cond 3: Si tiene mas de 125 es un zombie.

edad = 66

if edad < 18:
    print('Menor de edad')
elif edad <= 65:
    print('Mayor de edad, en edad de trabajar.')
elif edad <= 125:
    print('Mayor de edad, jubilado.')
else:
    print('Usted es un zombie')
print('Fin del programa.')