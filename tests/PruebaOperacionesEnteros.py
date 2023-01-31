import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros
class PruebaOperacionesEteros(unittest.TestCase):
    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_tresNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        numero3 = 30
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)
    def test_MCD_cuatroNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        numero3 = 30
        numero4 = 4
        resultadoEsperado = 2
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])
        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)