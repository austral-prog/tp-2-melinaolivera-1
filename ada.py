first_name = "AdA"
last_name = "LoVeLAce"

# Normalizar el formato
first_name_normalized = first_name.lower()
last_name_normalized = last_name.lower()

# Crear los distintos formatos
formatted1 = f"{first_name_normalized} {last_name_normalized}"
formatted2 = f"{first_name.capitalize()} {last_name.capitalize()}"
formatted3 = f"{first_name.upper()} {last_name.upper()}"
formatted4 = f"\t{first_name_normalized} {last_name_normalized}"

# Imprimir los resultados
print(formatted1)
print(formatted2)
print(formatted3)
print(formatted4)
