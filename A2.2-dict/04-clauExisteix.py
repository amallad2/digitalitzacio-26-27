#4. Comprovar si una clau existeix
#Demana un país a l’usuari i busca’n la capital de dues maneres: 
# (a) amb if pais in capital_pais; 
# (b) amb get() i un valor per defecte. Si no hi és, mostra "No tinc aquest país".
capital_pais = {"Espanya": "Madrid", "França": "París", "Itàlia": "Roma"}
pais="Japo"
# a)
if pais in capital_pais.keys():
   print("la capital de ",pais," és ", capital_pais[pais],".")
else:
   print("No tinc aquest país.")

# b)
capital=capital_pais.get(pais,"No tinc aquest país")
if capital!="No tinc aquest país":
    print("la capital de ",pais," és ", capital,".")
else:
    print("la capital de ",pais," és ", capital_pais[pais],".")