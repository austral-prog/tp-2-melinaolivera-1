def mostrar_nombres(first_name, last_name):
   
    lowercase_name = f"{first_name.lower()} {last_name.lower()}"
    capitalized_name = f"{first_name.title()} {last_name.title()}"
    uppercase_name = f"{first_name.upper()} {last_name.upper()}"


    print(f"       {lowercase_name}")
    print(capitalized_name)
    print(uppercase_name)
    print(f"\t{lowercase_name}")
