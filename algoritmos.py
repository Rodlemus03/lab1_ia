from colas import ColaFIFO, ColaLIFO, ColaPrioridad

def bfs(grafo, inicio, meta):
    cola = ColaFIFO()
    cola.agregar((inicio, [inicio]))
    visitados = set()
    while not cola.vacia():
        nodo, camino = cola.extraer()
        if nodo == meta:
            return camino
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, _ in grafo.get(nodo, []):
                cola.agregar((vecino, camino + [vecino]))
    return None

def dfs(grafo, inicio, meta):
    pila = ColaLIFO()
    pila.agregar((inicio, [inicio]))
    visitados = set()
    while not pila.vacia():
        nodo, camino = pila.extraer()
        if nodo == meta:
            return camino
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, _ in grafo.get(nodo, []):
                pila.agregar((vecino, camino + [vecino]))
    return None

def ucs(grafo, inicio, meta):
    cola = ColaPrioridad()
    cola.agregar(0, inicio, [inicio])
    visitados = set()
    while not cola.vacia():
        costo, nodo, camino = cola.extraer()
        if nodo == meta:
            return camino
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, peso in grafo.get(nodo, []):
                cola.agregar(costo + peso, vecino, camino + [vecino])
    return None

def greedy_best_first(grafo, heuristica, inicio, meta):
    cola = ColaPrioridad()
    cola.agregar(heuristica[inicio], inicio, [inicio])
    visitados = set()
    while not cola.vacia():
        _, nodo, camino = cola.extraer()
        if nodo == meta:
            return camino
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, _ in grafo.get(nodo, []):
                cola.agregar(heuristica.get(vecino, float('inf')), vecino, camino + [vecino])
    return None

def a_estrella(grafo, heuristica, inicio, meta):
    cola = ColaPrioridad()
    cola.agregar(heuristica[inicio], inicio, [inicio])
    visitados = set()
    while not cola.vacia():
        costo, nodo, camino = cola.extraer()
        if nodo == meta:
            return camino
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, peso in grafo.get(nodo, []):
                g_costo = costo + peso
                f_costo = g_costo + heuristica.get(vecino, float('inf'))
                cola.agregar(f_costo, vecino, camino + [vecino])
    return None
