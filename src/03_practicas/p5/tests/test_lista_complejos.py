"""Programa de pruebas de las funciones de `lista_complejos.py`."""

from io import StringIO
import sys
import complejos

stdin_backup = sys.stdin
stdout_backup = sys.stdout
sys.stdin = StringIO("1\n1\n2\n")
sys.stdout = StringIO()

import lista_complejos

sys.stdin = stdin_backup
sys.stdout = stdout_backup

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


def check_generar_complejo_aleatorio(x, y):
    c = lista_complejos.generar_complejo_aleatorio(x, y)
    check(
        x <= c.real <= y and x <= c.imag <= y,
        f"generar_complejo_aleatorio({x}, {y}): El complejo {c} no está en el rango [{x}, {y}]",
    )


def check_generar_lista_complejos(n, x, y):
    lista = lista_complejos.generar_lista_complejos(n, x, y)
    check(
        len(lista) == n,
        f"generar_lista_complejos({n}, {x}, {y}): La lista no tiene {n} elementos",
    )
    for i in range(n):
        c = lista[i]
        if not (x <= c.real <= y and x <= c.imag <= y):
            check(
                False,  # Force a failure
                f"generar_lista_complejos({n}, {x}, {y}): El complejo en la posición {i} ({c}) no está en el rango [{x}, {y}]",
            )


def check_str_lista_complejos(lista, esperado):
    res = lista_complejos.str_lista_complejos(lista)
    check(
        res == esperado,
        f"str_lista_complejos({lista}): Esperado {quote(esperado)}, obtenido {quote(res)}",
    )


def check_minimo_lista_complejos(lista, esperado):
    res = lista_complejos.minimo_lista_complejos(lista)
    check(
        res == esperado,
        f"minimo_lista_complejos({lista}): Esperado {quote(esperado)}, obtenido {quote(res)}",
    )


def check_suma_lista_complejos(lista, real, imag):
    res = lista_complejos.suma_lista_complejos(lista)
    check(
        aprox(res.real, real) and aprox(res.imag, imag),
        f"suma_lista_complejos({lista}): Esperado [{real}, {imag}], obtenido [{res.real}, {res.imag}]",
    )


def check_filtrar_primer_cuadrante(lista, esperado):
    res = lista_complejos.filtrar_primer_cuadrante(lista)
    check(len(res) == len(esperado), f"filtrar_primer_cuadrante({lista}): Longitud esperada {len(esperado)}, obtenida {len(res)}")
    check(
        res == esperado,
        f"filtrar_primer_cuadrante({lista}): Esperado {quote(esperado)}, obtenido {quote(res)}",
    )


for _ in range(10):
    check_generar_complejo_aleatorio(0, 1)
    check_generar_complejo_aleatorio(1, 5)
    check_generar_complejo_aleatorio(-10, 10)

check_generar_lista_complejos(0, 5, 0)
check_generar_lista_complejos(0, 5, 1)
check_generar_lista_complejos(0, 5, 3)

l1 = [complejos.Complejo(1, 2)]
l2 = [complejos.Complejo(3, 4), complejos.Complejo(1, 2)]
l3 = [complejos.Complejo(1, 2), complejos.Complejo(3, 4), complejos.Complejo(0, -0.1111111)]
l4 = [complejos.Complejo(-1, 1), complejos.Complejo(2, 2), complejos.Complejo(3, 3)]

check_str_lista_complejos([], "")
check_str_lista_complejos(l1, "1+2i")
check_str_lista_complejos(l2, "3+4i, 1+2i")
check_str_lista_complejos(l3, "1+2i, 3+4i, 0-0.1111i")

check_minimo_lista_complejos([], None)
check_minimo_lista_complejos(l1, l1[0])
check_minimo_lista_complejos(l2, l2[1])
check_minimo_lista_complejos(l3, l3[2])
check_minimo_lista_complejos(l4, l4[0])

check_suma_lista_complejos([], 0, 0)
check_suma_lista_complejos(l1, 1, 2)
check_suma_lista_complejos(l2, 4, 6)
check_suma_lista_complejos(l3, 4, 5.88888888)
check_suma_lista_complejos(l4, 4, 6)

check_filtrar_primer_cuadrante([], [])
check_filtrar_primer_cuadrante(l1, l1)
check_filtrar_primer_cuadrante(l2, l2)
check_filtrar_primer_cuadrante(l3, [l3[0], l3[1]])
check_filtrar_primer_cuadrante(l4, [l4[1], l4[2]])

end()
