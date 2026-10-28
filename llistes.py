llista=[2,5,8]

# Com accedim als elements de la llista
print(llista[0]) # Accedim al primer element
print(llista[1]) # Accedim al segon element
print(llista[2]) # Accedim al tercer element

# reccorregut de la llista amb un bucle for
for x in llista:
    print(x)

for x in range(len(llista)):
    print("Posició:" , x, " Contingut:",  llista[x])

llista.append(10)   #afegim un element al final de la llista
print(llista)
llista.insert(1,300) #afegim un element a la posició 1
print(llista)
# eliminar elements
del llista[2] #eliminem l'element de la posició 2
print(llista)
#update element
llista[1]=100 #modifiquem l'element de la posició 1