# content of test_sysexit.py
import pytest
import random
from solucion import *

exponenteMaximo = 100
baseMaxima = 100
iteracionesMaximas = 10000

def eq(a,b,eps=0.00001):
    return abs(a - b) <= eps

class TestClass:
    """
        Test de 0 elevado a un exponente aleatorio entre 0 y exponenteMaximo
    """
    def test_cero_exponente(self):
        base = 0
        for i in range (iteracionesMaximas):
            exponente = random.randint(0, exponenteMaximo)
            resultado = problemaRecursivo(base,exponente)
            #print(base,exponente,"=",resultado)
            assert resultado == base**exponente

    """
        Test de 1 elevado a un exponente aleatorio entre 0 y exponenteMaximo
    """
    def test_uno_exponente(self):
        base = 1
        for i in range (iteracionesMaximas):
            exponente = random.randint(0, exponenteMaximo)
            resultado = problemaRecursivo(base,exponente)
            #print(base,exponente,"=",resultado)
            assert resultado == base**exponente

    """
        Test de un numero aleatorio entre 0 y baseMaxima elevado a un exponente aleatorio entre 0 y exponenteMaximo
    """
    def test_base_exponente(self):
        for i in range (iteracionesMaximas):
            base = random.randint(0, baseMaxima)
            exponente = random.randint(0, exponenteMaximo)
            resultado = problemaRecursivo(base,exponente)
            assert base**exponente == resultado

    """
        Test de un numero aleatorio entre -baseMaxima y 0 elevado a un exponente aleatorio entre -exponenteMaximo y 0
    """
    def test_negativo(self):
        for i in range (iteracionesMaximas):
            base = random.randint(baseMaxima*-1, 0)
            exponente = random.randint(exponenteMaximo*-1, 0)
            resultado = problemaRecursivo(base,exponente)
            if(base==0 and exponente < 0):
                assert None == resultado
            else:
                assert (base**exponente == resultado) or (eq(resultado,base**exponente))
    """
        Test de un numero aleatorio entre -baseMaxima y baseMaxima elevado a un exponente aleatorio entre -exponenteMaximo y exponenteMaximo
    """
    def test_completo(self):
        for i in range (iteracionesMaximas):
            base = random.randint(baseMaxima*-1, baseMaxima)
            exponente = random.randint(exponenteMaximo*-1, exponenteMaximo)
            resultado = problemaRecursivo(base,exponente)
            if(base==0 and exponente < 0):
                assert None == resultado
            else:
                assert (base**exponente == resultado) or (eq(resultado,base**exponente))
