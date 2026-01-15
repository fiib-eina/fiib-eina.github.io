import horas

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


def check_hora_en_palabras(hora, esperado):
    res = horas.hora_en_palabras(hora)
    check(
        res == esperado,
        f"hora_en_palabras({hora}): Esperado {esperado}, obtenido {res}",
    )


def check_minutos_en_palabras(minutos, esperado):
    res = horas.minutos_en_palabras(minutos)
    check(
        res == esperado,
        f"minutos_en_palabras({minutos}): Esperado {esperado}, obtenido {res}",
    )


def check_periodo_del_dia(hora, esperado):
    res = horas.periodo_del_dia(hora)
    check(
        res == esperado,
        f"periodo_del_dia({hora}): Esperado {esperado}, obtenido {res}",
    )


def check_leer_hora(hora, minutos, esperado):
    res = horas.leer_hora(hora, minutos)
    check(
        res == esperado,
        f"leer_hora({hora}, {minutos}): Esperado {esperado}, obtenido {res}",
    )


check_hora_en_palabras(1, "La una")
check_hora_en_palabras(2, "Las dos")
check_hora_en_palabras(3, "Las tres")
check_hora_en_palabras(4, "Las cuatro")
check_hora_en_palabras(5, "Las cinco")
check_hora_en_palabras(6, "Las seis")
check_hora_en_palabras(7, "Las siete")
check_hora_en_palabras(8, "Las ocho")
check_hora_en_palabras(9, "Las nueve")
check_hora_en_palabras(10, "Las diez")
check_hora_en_palabras(11, "Las once")
check_hora_en_palabras(12, "Las doce")
check_hora_en_palabras(13, "La una")
check_hora_en_palabras(14, "Las dos")
check_hora_en_palabras(15, "Las tres")
check_hora_en_palabras(16, "Las cuatro")
check_hora_en_palabras(17, "Las cinco")
check_hora_en_palabras(18, "Las seis")
check_hora_en_palabras(19, "Las siete")
check_hora_en_palabras(20, "Las ocho")
check_hora_en_palabras(21, "Las nueve")
check_hora_en_palabras(22, "Las diez")
check_hora_en_palabras(23, "Las once")
check_hora_en_palabras(24, "Las doce")

check_minutos_en_palabras(0, "")
check_minutos_en_palabras(15, "y cuarto")
check_minutos_en_palabras(30, "y media")
check_minutos_en_palabras(45, "menos cuarto")

check_periodo_del_dia(1, "de la madrugada")
check_periodo_del_dia(6, "de la mañana")
check_periodo_del_dia(12, "del mediodía")
check_periodo_del_dia(15, "de la tarde")
check_periodo_del_dia(19, "de la noche")

check_leer_hora(1, 0, "La una de la madrugada")
check_leer_hora(3, 0, "Las tres de la madrugada")
check_leer_hora(3, 15, "Las tres y cuarto de la madrugada")
check_leer_hora(3, 30, "Las tres y media de la madrugada")
check_leer_hora(3, 45, "Las cuatro menos cuarto de la madrugada")
check_leer_hora(5, 45, "Las seis menos cuarto de la madrugada")
check_leer_hora(6, 0, "Las seis de la mañana")
check_leer_hora(12, 0, "Las doce del mediodía")
check_leer_hora(13, 0, "La una del mediodía")
check_leer_hora(15, 0, "Las tres de la tarde")
check_leer_hora(19, 0, "Las siete de la noche")
check_leer_hora(24, 0, "Las doce de la noche")

end()
