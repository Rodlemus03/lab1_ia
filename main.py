from utilities import cargar_datos
from algoritmos import bfs, dfs, ucs, greedy_best_first, a_estrella
class Nodo:
    def __init__(self, estado, accion=None, padre=None, costo_acumulado=0):
        self.estado = estado
        self.accion = accion
        self.padre = padre
        self.costo_acumulado = costo_acumulado


def main():
    archivo_costos = "funcion_de_costo.xlsx"
    archivo_heuristica = "heuristica.xlsx"
    grafo, heuristica = cargar_datos(archivo_costos, archivo_heuristica)
    
    inicio, meta = "Warm-up activities", "Stretching"
    
    while True:
        print("\nSeleccione un algoritmo:")
        print("1. Búsqueda en Anchura (BFS)")
        print("2. Búsqueda en Profundidad (DFS)")
        print("3. Costo Uniforme (UCS)")
        print("4. Greedy Best-First")
        print("5. A*")
        print("6. Salir")

        

        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            print("Ruta encontrada (BFS):", bfs(grafo, inicio, meta))
        elif opcion == "2":
            print("Ruta encontrada (DFS):", dfs(grafo, inicio, meta))
        elif opcion == "3":
            print("Ruta encontrada (UCS):", ucs(grafo, inicio, meta))
        elif opcion == "4":
            print("Ruta encontrada (Greedy Best-First):", greedy_best_first(grafo, heuristica, inicio, meta))
        elif opcion == "5":
            print("Ruta encontrada (A*):", a_estrella(grafo, heuristica, inicio, meta))
        elif opcion == "6":
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
