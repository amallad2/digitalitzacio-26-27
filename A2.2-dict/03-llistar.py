# 3. Iterar per claus i valors
# Crea capital_pais = {"Espanya": "Madrid", "França": "París", "Itàlia": "Roma"} i mostra cada parella amb aquest format:
# La capital de Espanya és Madrid.
capital_pais = {"Espanya": "Madrid", "França": "París", "Itàlia": "Roma"}

for clau,valor in capital_pais.items():
    print(f"La capital de {clau} és {valor}.")
    print("la capital de ",clau," és ", valor,".")