def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}")
    change= money - expense
    intchange= int((change - int(change))* 100)
    print()
    print("Vuelto")
    print()
    print(f"Pesos:\n{int(change)}")
    print(f"Centavos:\n{intchange}")
