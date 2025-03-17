import tartaglia

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


def test_coeficiente_binomial(n, k, esperado):
    res = tartaglia.coeficiente_binomial(n, k)
    check(
        res == esperado,
        f"coeficiente_binomial({n}, {k}): Esperado {esperado}, obtenido {res}",
    )


test_coeficiente_binomial(0, 0, 1)
test_coeficiente_binomial(1, 0, 1)
test_coeficiente_binomial(1, 1, 1)
test_coeficiente_binomial(2, 0, 1)
test_coeficiente_binomial(2, 1, 2)
test_coeficiente_binomial(2, 2, 1)
test_coeficiente_binomial(3, 0, 1)
test_coeficiente_binomial(3, 1, 3)
test_coeficiente_binomial(3, 2, 3)
test_coeficiente_binomial(3, 3, 1)
test_coeficiente_binomial(4, 0, 1)


end()
