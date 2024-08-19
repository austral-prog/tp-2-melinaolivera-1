def change():
    gasto = float(input("Ingresar gasto:\n"))
dinero_recibido = float(input("Dinero recibido\n"))
vuelto = dinero_recibido - gasto
pesos = int(vuelto)
centavos = round((vuelto - pesos) * 100)
print("\nVuelto\n")
print(f"Pesos:\n{pesos}")
print(f"Centavos:\n{centavos}")
