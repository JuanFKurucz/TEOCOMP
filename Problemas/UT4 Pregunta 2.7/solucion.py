def problemaRecursivo(base,exponente):
    if exponente == 1:
        return base
    elif exponente == 0:
        return 1
    if exponente % 2 != 0:
        exponente-=1
        return base * problemaRecursivo(base,exponente)
    else:
        exponente/=2
        return problemaRecursivo(base,exponente) * problemaRecursivo(base,exponente)
