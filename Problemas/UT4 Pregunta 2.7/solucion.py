def potenciacionOptimaRecurisva(base,exponente):
    if exponente < 0:
        if base == 0:
            return None
        return 1 / potenciacionOptimaRecurisva(base,exponente*-1)
    if exponente == 1:
        return base
    elif exponente == 0:
        return 1
    if exponente % 2 != 0:
        exponente-=1
        return base * potenciacionOptimaRecurisva(base,exponente)
    else:
        exponente/=2
        return potenciacionOptimaRecurisva(base,exponente) * potenciacionOptimaRecurisva(base,exponente)
