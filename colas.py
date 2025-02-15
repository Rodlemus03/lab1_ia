import heapq


class ColaFIFO:
    def __init__(self):
        self.cola = []
    
    def vacia(self):
        return not self.cola
    
    def extraer(self):
        return self.cola.pop(0) if self.cola else None
    
    def agregar(self, elemento):
        self.cola.append(elemento)

class ColaLIFO:
    def __init__(self):
        self.pila = []
    
    def vacia(self):
        return not self.pila
    
    def extraer(self):
        return self.pila.pop() if self.pila else None
    
    def agregar(self, elemento):
        self.pila.append(elemento)

class ColaPrioridad:
    def __init__(self):
        self.cola = []
    
    def vacia(self):
        return not self.cola
    
    def extraer(self):
        return heapq.heappop(self.cola) if self.cola else None
    
    def agregar(self, prioridad, nodo, camino):
        heapq.heappush(self.cola, (prioridad, nodo, camino))