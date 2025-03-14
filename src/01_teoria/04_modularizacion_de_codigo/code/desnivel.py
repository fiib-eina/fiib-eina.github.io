def obtener_altura(checkpoint_num):
    print(f"Checkpoint {checkpoint_num} - Altura:", end=" ")
    altura = int(input())
    return altura


def es_altura_valida(h):
    return 0 < h < 8848


def obtener_altura_valida(checkpoint_num):
    altura = obtener_altura(checkpoint_num)
    while not es_altura_valida(altura):
        print("Altura no válida!")
        altura = obtener_altura(checkpoint_num)
    return altura


def desnivel_positivo(h1, h2):
    if h2 > h1:
        desnivel = h2 - h1
    else:
        desnivel = 0
    return desnivel


def desnivel_absoluto(h1, h2):
    return abs(h2 - h1)


def desniveles_totales():
    # Obtener los dos primeros checkpoints
    h1 = obtener_altura_valida(1)
    h2 = obtener_altura_valida(2)
    # Inicializar desnivel y checkpoint (a 3)
    total_positivo = 0
    total_acumulado = 0
    checkpoint_num = 3
    while h1 != h2:
        total_positivo += desnivel_positivo(h1, h2)
        total_acumulado += desnivel_absoluto(h1, h2)
        # Actualizar checkpoint
        checkpoint_num += 1
        # Actualizar alturas
        h1 = h2
        h2 = obtener_altura_valida(checkpoint_num + 1)
    print(f"Desnivel positivo: {total_positivo}m")
    print(f"Desnivel acumulado: {total_acumulado}m")


desniveles_totales()
