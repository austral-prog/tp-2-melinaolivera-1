def change():
  gasto = float(input("Ingresar gasto:\n"))
  dinero_recibido = float(input("Dinero recibido\n"))
  vuelto_total = dinero_recibido - gasto
  pesos = int(vuelto_total)
  centavos = int(round((vuelto_total - pesos) * 100))
  print("\nVuelto\n")
  print(f"Pesos:\n{pesos}")
  print(f"Centavos:\n{centavos}")
