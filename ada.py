def mostrar_nombres(first_name, last_name):
    # Formatos de nombres
    lowercase_name = f"{first_name.lower()} {last_name.lower()}"
    capitalized_name = f"{first_name.title()} {last_name.title()}"
    uppercase_name = f"{first_name.upper()} {last_name.upper()}"

    # Imprimir los resultados en los formatos solicitados
    print(lowercase_name)
    print(capitalized_name)
    print(uppercase_name)
    print(f"\t{lowercase_name}")
