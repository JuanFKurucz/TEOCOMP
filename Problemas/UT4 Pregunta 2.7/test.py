# content of test_sysexit.py
import pytest
import random
from solucion import *

exponenteMaximo = 10
baseMaxima = 10
iteracionesMaximas = 100

class TestClass:
    """
        Test de 0 elevado a un exponente aleatorio entre 0 y exponenteMaximo
    """
    def test_cero_exponente(self):
        base = 0
        for i in range (iteracionesMaximas):
            exponente = random.randint(0, exponenteMaximo)
            resultado = problemaRecursivo(base,exponente)
            print(base,exponente,"=",resultado)
            assert resultado == 0

    """
        Test de 1 elevado a un exponente aleatorio entre 0 y exponenteMaximo
    """
    def test_uno_exponente(self):
        base = 1
        for i in range (iteracionesMaximas):
            exponente = random.randint(0, exponenteMaximo)
            resultado = problemaRecursivo(base,exponente)
            print(base,exponente,"=",resultado)
            assert resultado == 1

    """
        Test de un numero aleatorio entre o y baseMaxima elevado a un exponente aleatorio entre 0 y exponenteMaximo
    """
    def test_base_exponente(self):
        for i in range (iteracionesMaximas):
            base = random.randint(0, baseMaxima)
            exponente = random.randint(0, exponenteMaximo)
            resultado = problemaRecursivo(base,exponente)
            print(base,exponente,"=",resultado)
            assert base**exponente == resultado
