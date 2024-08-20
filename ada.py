def change():
    
    print("Ingresar gasto:")
    gasto = float(input())
    
    print("Dinero recibido")
    dinero_recibido = float(input())

    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print("")  
    print("Vuelto")
    print("")  
    print(f"Pesos:")
    print(f"{pesos}")
    print(f"Centavos:")
    print(f"{centavos}")
