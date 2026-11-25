cotxe={"marca": "Toyota", "model": "Corolla", "any": 2020}

print(cotxe["marca"])  # Output: Toyota
print(cotxe.get("potencia","No disponible"))  # Output: No disponible

if "potencia" in cotxe.keys():
    print(cotxe["potencia"])  # Output: Corolla
else:
    print("No disponible")  # Output: No disponible