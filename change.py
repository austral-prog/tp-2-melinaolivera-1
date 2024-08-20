gasto = float(input("Ingresar gasto:\n"))
dinero_recibido = float(input("Dinero recibido:\n"))

vuelto = dinero_recibido - gasto
pesos = int(vuelto)
centavos = int(round((vuelto - pesos) * 100))

print("\nVuelto")
print(f"Pesos: {pesos}")
print(f"Centavos: {centavos}")
