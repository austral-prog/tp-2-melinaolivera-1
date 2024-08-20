def comparar_paises(pais_x, pais_y):
    resultado_x_primero = pais_x < pais_y
    resultado_y_primero = pais_y < pais_x

    print(f"The result of {pais_x} comes first in the dictionary than {pais_y} is {resultado_x_primero}.")
    print(f"The result of {pais_y} comes first in the dictionary than {pais_x} is {resultado_y_primero}.")

pais_x = "Bangladesh"
pais_y = "Barbados"

comparar_paises(pais_x, pais_y)
