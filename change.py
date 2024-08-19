
def calcular_vuelto(gasto, recibido):
    vuelto_total = recibido - gasto
    pesos = int(vuelto_total)
    centavos = int(round((vuelto_total - pesos) * 100))
    print("Ingresar gasto:")
    print(f"{gasto:.2f}")
    print("Dinero recibido")
    print(f"{recibido:.2f}")
    print("")  # Línea vacía
    print("Vuelto")
    print("")  # Línea vacía
    print("Pesos:")
    print(f"{pesos}")
    print("Centavos:")
    print(f"{centavos}")
