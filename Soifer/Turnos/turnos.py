print('**************************')
print('*Sistema de Turnos PyTurn*')
print('**************************')
usuario1 = 'Juan'
password1 = '1234'
usuario2 = 'Pepe'
password2 = '9876'
usuario = input('Ingrese su usuario: ')
password = input('Ingrese su contraseña: ')
medico1 = 'Jorge Perez'
medico2 = 'Cristina Ramos'
if (usuario == usuario1 and password == password1) or (usuario == usuario2 and password == password2):
    print('Bienvenido al sistema de turnos médicos ' + usuario + '.')
    if usuario == 'Juan':
        #print('Su medico es ' + medico1 + '.')
        medico = medico1    
    else:
        #print('Su medico es ' + medico2 + '.')
        medico = medico2
    print('Su medico es: '+ medico + '.')
else:
    print('Usted no tiene acceso al sistema de turnos.')








