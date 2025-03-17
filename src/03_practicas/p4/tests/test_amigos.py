import amigos


errs = 0


def check(condicion, error_msg):
    global errs
    if not condicion:
        print(f"-- ERROR: {error_msg}")
        errs += 1


def end():
    global errs
    if errs == 0:
        print("OK: 0 errores")
    else:
        print(f"FAIL: {errs} errores")


def check_suma_divisores_propios(n, esperado):
    res = amigos.suma_divisores_propios(n)
    check(
        res == esperado,
        f"suma_divisores_propios({n}): Esperado {esperado}, obtenido {res}",
    )


def check_son_amigos(n, m, esperado):
    res = amigos.son_amigos(n, m)
    check(
        res == esperado,
        f"son_amigos({n}, {m}): Esperado {esperado}, obtenido {res}",
    )


check_suma_divisores_propios(24, 36)
check_suma_divisores_propios(220, 284)
check_suma_divisores_propios(284, 220)
check_suma_divisores_propios(1184, 1210)

check_son_amigos(220, 284, True)
check_son_amigos(284, 220, True)
check_son_amigos(220, 285, False)
check_son_amigos(220, 220, False)
check_son_amigos(1184, 1210, True)
check_son_amigos(1210, 1184, True)

end()
