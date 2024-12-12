
import unittest
from calculadora import calcular_imc

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calcular_imc(10, 1), 10)

if __name__ == "__main__":
    unittest.main()
