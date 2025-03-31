"""Programa de pruebas de las funciones del módulo `horas.py`."""

import complejos

errs = 0


def check(condicion, error_msg):
    global errs
    if not condicion:
        print(f"-- ERROR: {error_msg}")
        errs += 1


def aprox(a, b):
    return abs(a - b) < 0.0001


def quote(value):
    if isinstance(value, str):
        return f'"{value}"'
    return value


def end():
    global errs
    if errs == 0:
        print("OK: 0 errores")
    else:
        print(f"FAIL: {errs} errores")


def check_constructor(r, i, real, imag):
    c = complejos.Complejo(r, i)
    check(type(c) == complejos.Complejo, f"Complejo({r}, {i}) no es de tipo Complejo")
    check(c.real == real and c.imag == imag, f"Complejo({r}, {i}) != ({real}, {imag})")


def check_str_complejo(r, i, expected):
    c = complejos.Complejo(r, i)
    # check(complejos.str_complejo(c) == expected, f"str_complejo({c}) != {quote(expected)}")
    res = complejos.str_complejo(c)
    check(
        res == expected,
        f"str_complejo({c}): Esperado {quote(expected)}, obtenido {quote(res)}",
    )


def check_sumar(r1, i1, r2, i2, r3, i3):
    c1 = complejos.Complejo(r1, i1)
    c2 = complejos.Complejo(r2, i2)
    c3 = complejos.Complejo(r3, i3)
    # check(complejos.sumar(c1, c2) == c3, f"sumar({c1}, {c2}) != {quote(c3)}")
    res = complejos.sumar(c1, c2)
    check(
        res == c3,
        f"sumar({c1}, {c2}): Esperado {quote(c3)}, obtenido {quote(res)}",
    )


def check_restar(r1, i1, r2, i2, r3, i3):
    c1 = complejos.Complejo(r1, i1)
    c2 = complejos.Complejo(r2, i2)
    c3 = complejos.Complejo(r3, i3)
    # check(complejos.restar(c1, c2) == c3, f"restar({c1}, {c2}) != {quote(c3)}")
    res = complejos.restar(c1, c2)
    check(
        res == c3,
        f"restar({c1}, {c2}): Esperado {quote(c3)}, obtenido {quote(res)}",
    )


def check_modulo(r, i, expected):
    c = complejos.Complejo(r, i)
    # check(aprox(complejos.modulo(c), expected), f"modulo({c}) !~= {quote(expected)}")
    res = complejos.modulo(c)
    check(
        aprox(res, expected),
        f"modulo({c}): Esperado {quote(expected)}, obtenido {quote(res)}",
    )


def check_compare(r1, i1, r2, i2, expected):
    c1 = complejos.Complejo(r1, i1)
    c2 = complejos.Complejo(r2, i2)
    # check(complejos.igual_que(c1, c2) == True, f"igual_que({c1}, {c2}) != True")
    res_menor = complejos.menor_que(c1, c2)
    res_mayor = complejos.mayor_que(c1, c2)
    res_igual = complejos.igual_que(c1, c2)

    check(
        res_menor == (expected == "menor"),
        f"menor_que({c1}, {c2}): Esperado {quote(expected == 'menor')}, obtenido {quote(res_menor)}",
    )
    check(
        res_mayor == (expected == "mayor"),
        f"mayor_que({c1}, {c2}): Esperado {quote(expected == 'mayor')}, obtenido {quote(res_mayor)}",
    )
    check(
        res_igual == (expected == "igual"),
        f"igual_que({c1}, {c2}): Esperado {quote(expected == 'igual')}, obtenido {quote(res_igual)}",
    )


check_constructor(0, 0, 0, 0)
check_constructor(1, 2, 1, 2)

check_str_complejo(0, 0, "0+0i")
check_str_complejo(4, 6, "4+6i")
check_str_complejo(-4, 6, "-4+6i")
check_str_complejo(4, -6, "4-6i")
check_str_complejo(-4, -6, "-4-6i")
check_str_complejo(3.22, 4.111111111111, "3.22+4.1111i")
check_str_complejo(3.22, -4.111111111111, "3.22-4.1111i")

check_sumar(0, 0, 0, 0, 0, 0)
check_sumar(1, 0, 0, 0, 1, 0)
check_sumar(0, 1, 0, 0, 0, 1)
check_sumar(1, 1, 1, 1, 2, 2)
check_sumar(1, 1, -1, -1, 0, 0)
check_sumar(1, 1, 1, -1, 2, 0)

check_restar(0, 0, 0, 0, 0, 0)
check_restar(1, 0, 0, 0, 1, 0)
check_restar(0, 1, 0, 0, 0, 1)
check_restar(1, 1, 1, 1, 0, 0)
check_restar(1, 1, -1, -1, 2, 2)
check_restar(1, 1, 1, -1, 0, 2)

check_modulo(0, 0, 0)
check_modulo(1, 0, 1)
check_modulo(0, 1, 1)
check_modulo(1, 1, 1.41421)
check_modulo(1, -1, 1.41421)
check_modulo(-1, 1, 1.41422)
check_modulo(-1, -1, 1.41421)
check_modulo(1, 2, 2.23607)
check_modulo(1, -2, 2.23607)
check_modulo(-1, 2, 2.23607)
check_modulo(-1, -2, 2.23607)

check_compare(0, 0, 0, 0, "igual")
check_compare(1, 0, 0, 0, "mayor")
check_compare(0, 1, 0, 0, "mayor")
check_compare(0, 0, 1, 0, "menor")
check_compare(0, 0, 0, 1, "menor")
check_compare(1, 1, 1, 1, "igual")
check_compare(1, 1, 1, -1, "igual")
check_compare(1, 1, -1, 1, "igual")
check_compare(1, 1, -1, -1, "igual")
check_compare(1, 1, 2, 2, "menor")
check_compare(2, 2, 1, 1, "mayor")

end()
