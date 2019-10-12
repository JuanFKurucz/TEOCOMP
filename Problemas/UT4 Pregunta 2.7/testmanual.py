import numpy
from solucion import *
def printer(base,exponente):
    resultado = potenciacionOptimaRecurisva(base,exponente)
    esperado = base**exponente
    print (base,exponente," ==> ",resultado,"=",esperado," ==> ",resultado==esperado)

def testManual(base,rango,incremento=1):
    print ("Potencias de "+str(base))
    if int(incremento) == incremento:
        for i in range(rango*-1,rango,incremento):
            printer(base,i)
    else:
        for i in numpy.arange(rango*-1, rango, incremento):
            printer(base,i)
    print ("")

testManual(2,6)
testManual(-2,6)
testManual(5,6)
testManual(-5,6)
testManual(1/2,6)
testManual(-(1/2),6)
