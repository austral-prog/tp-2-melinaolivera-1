def comparar_paises(pais_x, pais_y):
    # Determina si pais_x viene antes que pais_y en el diccionario
    resultado_x_primero = pais_x < pais_y
    # Determina si pais_y viene antes que pais_x en el diccionario
    resultado_y_primero = pais_y < pais_x

    # Imprimir resultados con el formato requerido
    print(f"The result of {pais_x} comes first in the dictionary than {pais_y} is {str(resultado_x_primero).capitalize()}.")
    print(f"The result of {pais_y} comes first in the dictionary than {pais_x} is {str(resultado_y_primero).capitalize()}.")

# Definir los nombres de los países
pais_x = "Bangladesh"
pais_y = "Barbados"

# Llamar a la función para comparar los países
comparar_paises(pais_x, pais_y)

