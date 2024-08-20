def imprimir_informe_vuelto():
    # Solicitar entrada del usuario
    gasto = float(input("Ingresar gasto:\n"))
    dinero_recibido = float(input("Dinero recibido\n"))

    # Calcular el vuelto
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    # Imprimir el informe
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")

# Llamar a la función para ejecutar el programa
imprimir_informe_vuelto()
