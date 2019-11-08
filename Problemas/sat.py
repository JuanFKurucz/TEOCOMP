arbol = []
'''
arbol = [
    []
]
'''
import itertools
import random
#random.seed(30)

operadores = ["and","or","not"]

def auxiliar(lista,altura,minAltura,maxAltura,variables):
    global operadores
    operador = operadores[random.randint(0,len(operadores)-1)]
    if altura >= minAltura and random.randint(0,1) == 1:
        operador = variables[random.randint(0,len(variables)-1)]

    if altura < maxAltura and operador not in variables:
        lista.append(operador)
        if operador == "not":
            lista.append([])
            auxiliar(lista[1],altura+1,minAltura,maxAltura,variables)
        else:
            lista.append([])
            lista.append([])
            auxiliar(lista[1],altura+1,minAltura,maxAltura,variables)
            auxiliar(lista[2],altura+1,minAltura,maxAltura,variables)
    else:
        operador = variables[random.randint(0,len(variables)-1)]
        lista.append(operador)

def generarArbol(min,max,n):
    resultado = []
    auxiliar(resultado,0,min,max,n)
    return resultado

def evaluarRecursivo(lista,booleans):
    if len(lista)>1:
        valor1 = evaluarRecursivo(lista[1],booleans)
        if lista[0] == "and":
            valor2 = evaluarRecursivo(lista[2],booleans)
            return valor1 and valor2
        elif lista[0] == "or":
            valor2 = evaluarRecursivo(lista[2],booleans)
            return valor1 or valor2
        elif lista[0] == "not":
            return not valor1
    else:
        return booleans[lista[0]]

def allVarAssigns(n):
   return list(itertools.product(*([[False,True]]*n)))

def probarExaustivo(arbol,n):
    producto = allVarAssigns(n)
    #print(producto)
    for p in producto:
        resultado = evaluarRecursivo(arbol,p)
        if resultado:
            return True
    return False

def probar(n,topeIntentos):
    min = n//8
    max = n//2
    numeros = []
    for i in range(n):
        numeros.append(i)
    arbol = generarArbol(min,max,numeros)
    print(arbol)
    print("Exahustivo: "+str(probarExaustivo(arbol,n)))

    intentos = 0
    for intentos in range(topeIntentos):
        booleans = []
        for i in range(n):
            if random.randint(0,1) == 1:
                booleans.append(True)
            else:
                booleans.append(False)
        resultado = evaluarRecursivo(arbol,booleans)
        print(booleans)
        print(evaluarRecursivo(arbol,booleans))
        if resultado:
            break
    print("Termino")

probar(8,1000)
