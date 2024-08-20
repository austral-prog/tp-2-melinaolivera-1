import unittest

def calcular_vuelto(gasto, dinero_recibido):
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))
    return pesos, centavos

class TestVuelto(unittest.TestCase):
    def test_vuelto(self):
        self.assertEqual(calcular_vuelto(100, 150), (50, 0))
        self.assertEqual(calcular_vuelto(99.75, 100), (0, 25))

if __name__ == '__main__':
    unittest.main()
