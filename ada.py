def mostrar_nombres(first_name, last_name):
    # Convertir a minúsculas
    lowercase_name = f"{first_name.lower()} {last_name.lower()}"
    # Convertir a capitalizado
    capitalized_name = f"{first_name.title()} {last_name.title()}"
    # Convertir a mayúsculas
    uppercase_name = f"{first_name.upper()} {last_name.upper()}"
    
    # Imprimir los resultados en los formatos solicitados
    print(lowercase_name)
    print(capitalized_name)
    print(uppercase_name)
    print(f"\t{lowercase_name}")

# Variables de entrada
first_name = "AdA"
last_name = "LoVeLAce"

# Llamar a la función para mostrar los nombres
mostrar_nombres(first_name, last_name)
