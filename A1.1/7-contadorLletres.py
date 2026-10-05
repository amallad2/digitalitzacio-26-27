# Exemples recorrer cadenes
s="hola"
cont=0
for c in s:
    print(c)
    cont+=1  # cont = cont +1

print("Nombre de lletres ", cont , " o amb len = ", len(s))

for i in range(0,len(s)):
    print(i, s[i])