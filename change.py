import sys

def main(gasto, dinero_recibido):
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print("\nVuelto")
    print(f"Pesos: {pesos}")
    print(f"Centavos: {centavos}")

if __name__ == "__main__":
    gasto = float(sys.argv[1])
    dinero_recibido = float(sys.argv[2])
    main(gasto, dinero_recibido)
