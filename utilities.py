import pandas as pd


def cargar_datos(archivo_costos, archivo_heuristica):
    df_costos = pd.read_excel(archivo_costos)
    df_heuristica = pd.read_excel(archivo_heuristica)
    
    grafo = {}
    for _, fila in df_costos.iterrows():
        origen, destino, costo = fila["Origen"], fila["Destino"], fila["Cost"]
        grafo.setdefault(origen, []).append((destino, costo))
    
    heuristica = {fila["Activity"]: fila["Recovery time after burning 300cal (minutes)"] for _, fila in df_heuristica.iterrows()}
    
    return grafo, heuristica