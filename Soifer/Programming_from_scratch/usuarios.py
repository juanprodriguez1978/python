edad = int(input('Ingrese su edad: '))
nombre = input('Ingrese su nombre: ')
password = input('Ingrese su password: ')

if edad >= 18:
    print('Mayor de edad')
else:
    print('Menor de edad')

# if nombre == 'Juan':
#     if password == '123456':
#         print('Ingresa al sistema.')
#     else:
#         print('No ingresa al sistema.')
# else:
#     print('No ingresa al sistema.')
    
#AND
if nombre == 'Juan' and password == '123456':
    print('Ingresa al sistema.')
else:
    print('No ingresa al sistema.')
