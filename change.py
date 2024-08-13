def change():
    gasto = float(input("ingresar gasto: "))
    dinero_recibido = float(input("ingresar el dinero recibido: "))
    vuelto = dinero_recibido - gasto
    print(f"vuelto:{vuelto}")
    pesos = int(vuelto)
    centavos =int((vuelto - pesos)*100)
    print(f"pesos:{pesos}")
    print(f"centavos:{centavos}")
