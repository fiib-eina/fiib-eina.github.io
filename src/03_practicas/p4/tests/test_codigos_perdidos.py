from io import StringIO
import codigos_perdidos
import sys

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


def test_sumar_cifras(n, esperado):
    res = codigos_perdidos.sumar_cifras(n)
    check(
        res == esperado,
        f"sumar_cifras({n}): Esperado {esperado}, obtenido {res}",
    )


def test_codigos_perdidos(min, max, esperado):
    # Workaround para evitar que se escriba en la consola
    tmp_stdout = sys.stdout
    sys.stdout = StringIO()
    res = codigos_perdidos.codigos_perdidos(min, max)
    sys.stdout = tmp_stdout
    check(
        res == esperado,
        f"codigos_perdidos({min}, {max}): Esperado {esperado}, obtenido {res}",
    )


test_sumar_cifras(123, 6)
test_sumar_cifras(1234, 10)
test_sumar_cifras(1, 1)
test_sumar_cifras(0, 0)
test_sumar_cifras(100, 1)

test_codigos_perdidos(-1, 20, -1)
test_codigos_perdidos(20, 10, -1)
test_codigos_perdidos(10, 20, 1)
test_codigos_perdidos(10, 99, 240)

end()
