opciones = ['a', 'b', 'c']
print(opciones)
opciones.append('d') #Agrego el elemento al final de la lista
print(opciones)
opc2 = ['z', 'j', 'k']
opciones.extend(opc2)
print(opciones)
opciones.extend(['e', 'x', 'y'])
print(opciones)
opciones.insert(1, 'L')#En el puesto 1 inserto una L
print(opciones)
opciones.remove('c')#Elimina la primera ocurrencia del valor
print(opciones)
opciones.pop()#Elimina el ultimo elemento de la ista
print(opciones)
opciones.sort()#Ordena la lista de menor a mayor
print(opciones)
opciones.sort(reverse=True)#Ordena la lista de mayor a menor
print(opciones)