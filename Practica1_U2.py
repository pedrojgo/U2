from collections import deque

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

def encontrar_cero(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                return i, j

def mover_izquierda(matriz):
    i, j = encontrar_cero(matriz)
    if j > 0:
        nueva_matriz = [fila[:] for fila in matriz]
        nueva_matriz[i][j], nueva_matriz[i][j - 1] = nueva_matriz[i][j - 1], nueva_matriz[i][j]
        return nueva_matriz
    return None

def mover_derecha(matriz):
    i, j = encontrar_cero(matriz)
    if j < 2:
        nueva_matriz = [fila[:] for fila in matriz]
        nueva_matriz[i][j], nueva_matriz[i][j + 1] = nueva_matriz[i][j + 1], nueva_matriz[i][j]
        return nueva_matriz
    return None

def mover_arriba(matriz):
    i, j = encontrar_cero(matriz)
    if i > 0:
        nueva_matriz = [fila[:] for fila in matriz]
        nueva_matriz[i][j], nueva_matriz[i - 1][j] = nueva_matriz[i - 1][j], nueva_matriz[i][j]
        return nueva_matriz
    return None

def mover_abajo(matriz):
    i, j = encontrar_cero(matriz)
    if i < 2:
        nueva_matriz = [fila[:] for fila in matriz]
        nueva_matriz[i][j], nueva_matriz[i + 1][j] = nueva_matriz[i + 1][j], nueva_matriz[i][j]
        return nueva_matriz
    return None

def resolver_puzzle(matriz_inicial, matriz_final):
    frontera = deque([(matriz_inicial, [])])
    explorados = set()

    while frontera:
        matriz_actual, camino = frontera.popleft()
        explorados.add(tuple(map(tuple, matriz_actual)))

        if matriz_actual == matriz_final:
            return camino

        for movimiento, nombre_movimiento in [(mover_izquierda, 'Izquierda'), (mover_derecha, 'Derecha'), (mover_arriba, 'Arriba'), (mover_abajo, 'Abajo')]:
            nueva_matriz = movimiento(matriz_actual)
            if nueva_matriz is not None and tuple(map(tuple, nueva_matriz)) not in explorados:
                nuevo_camino = camino + [nombre_movimiento]
                frontera.append((nueva_matriz, nuevo_camino))

    return None

matriz_inicial = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

matriz_final = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

camino = resolver_puzzle(matriz_inicial, matriz_final)

if camino is not None:
    costo_total = len(camino)
    coordenadas_finales = encontrar_cero(matriz_inicial)
    for i, movimiento in enumerate(camino, start=1):
        print(f"Paso {i}: Mover {movimiento}")
        matriz_inicial = {
            'Izquierda': mover_izquierda,
            'Derecha': mover_derecha,
            'Arriba': mover_arriba,
            'Abajo': mover_abajo
        }[movimiento](matriz_inicial)
        mostrar_matriz(matriz_inicial)
        coordenadas_finales = encontrar_cero(matriz_inicial)
        print(f"Costo parcial de los movimientos: {i}")
        print(f"Cordenadas parciales de la posición del valor 7: {coordenadas_finales}")

    print(f"Costo total de los movimientos: {costo_total}")
    print(f"Cordenadas finales de la posición del valor 7: {coordenadas_finales}")
else:
    print("No se encontró una solución.")
