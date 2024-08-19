def change():
    gasto = float(input("Ingresar gasto:\n"))
    dinero_recibido = float(input("Dinero recibido\n"))
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int((vuelto - pesos) * 100)
    print(f"\nVuelto\n\nPesos:\n{pesos}\nCentavos:\n{centavos}")
