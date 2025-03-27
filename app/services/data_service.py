import pandas as pd
import numpy as np
from typing import List
from app.models.station import Station

def load_data(file_path: str) -> List[Station]:
    df = pd.read_excel(file_path)
    print("Datos cargados desde el archivo:", df.head())  # Esto imprimirá las primeras filas del dataframe


    df.columns = df.columns.str.strip()

    df.rename(columns={
        'CÓDIGO': 'codigo',
        'DESCRIPCIÓN': 'nombre',
        'LATITUD': 'latitud',
        'LONGITUD': 'longitud',
        'DIRECCIÓN': 'direccion',
        'C.P.': 'cp',
        'POBLACION': 'poblacion',
        'PROVINCIA': 'provincia',
        'PAIS': 'pais'
    }, inplace=True)

    print("Columnas después de renombrar:", df.columns)
    
    df['direccion'] = df['direccion'].apply(lambda x: x.strip() if isinstance(x, str) else x)


    df.replace([pd.NA, np.nan, float('inf'), -float('inf')], None, inplace=True)
    
    df['codigo'] = df['codigo'].apply(lambda x: str(x) if x is not None else '')
    df['cp'] = df['cp'].apply(lambda x: str(x) if x is not None else '')

    
    return [Station(**row) for row in df.to_dict(orient="records")]

def get_all_items(file_path: str) -> List[Station]:
    return load_data(file_path)

def get_item_by_codigo(file_path: str, codigo: str):
    items = load_data(file_path)
    for item in items:
        if item.codigo == codigo:
            return item
    return None

def search_by_direccion(file_path: str, direccion: str) -> List[Station]:
    # Verificar que el término de búsqueda tenga al menos 3 caracteres
    if len(direccion) < 3:
        raise ValueError("El término de búsqueda debe tener al menos 3 caracteres")
    
    # Cargar los datos
    print("Cargando los datos desde el archivo...")
    items = load_data(file_path)
    print(f"Datos cargados: {len(items)} estaciones")
    
    # Filtrar los items cuya dirección contenga el término de búsqueda
    filtered_items = [item for item in items if item.direccion and len(item.direccion) >= 3 and direccion.lower() in item.direccion.lower()]
    print(f"Filtrado {len(filtered_items)} estaciones con la dirección que contiene '{direccion}'")
    
    return filtered_items

def search_by_poblacion(file_path: str, poblacion: str) -> List[Station]:
    # Cargar los datos
    print("Cargando los datos desde el archivo...")
    items = load_data(file_path)
    print(f"Datos cargados: {len(items)} estaciones")

    # Filtrar por población
    filtered_items = [
        item for item in items if item.poblacion and poblacion.lower() in item.poblacion.lower()
    ]
    print(f"Filtradas {len(filtered_items)} estaciones en la población '{poblacion}'")

    return filtered_items
