
import unittest
from calculadora import calcular_imc

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calcular_imc(65, 1.74), 21.47)

if __name__ == "__main__":
    unittest.main()
