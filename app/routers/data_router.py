from fastapi import APIRouter, HTTPException
from typing import List
from app.services.data_service import get_all_items, get_item_by_codigo, search_by_direccion, search_by_poblacion
from app.models.station import Station

router = APIRouter()

file_path = r"C:\projects\fastapi_train_project\app\data\listado_completo_av_ld_md.xlsx"

@router.get("/stations", response_model=List[Station])
def get_data():
    print("El servidor está funcionando correctamente.") 
    return get_all_items(file_path)

@router.get("/station/{codigo}", response_model=Station)
def get_data_by_codigo(codigo: str):
    item = get_item_by_codigo(file_path, codigo)
    if item is None:
        raise HTTPException(status_code=404, detail="Station no encontrado")
    return item

@router.get("/station/search/direccion/{direccion}", response_model=List[Station])
def search_direccion(direccion: str):
    print(f"Recibiendo búsqueda por dirección: {direccion}")
    
    # Verificar si el término de búsqueda tiene al menos 3 caracteres
    if len(direccion) < 3:
        print(f"El término de búsqueda tiene menos de 3 caracteres: {direccion}")
        raise ValueError("El término de búsqueda debe tener al menos 3 caracteres")
    
    # Buscar los elementos que coinciden con la dirección
    items = search_by_direccion(file_path, direccion)
    print(f"Items encontrados: {len(items)}")
    
    # Si no hay elementos que coincidan, lanzar un error
    if not items:
        print(f"No se encontraron resultados para la dirección: {direccion}")
        raise HTTPException(status_code=404, detail="No se encontraron resultados para la dirección proporcionada")
    
    # Si se encuentran los elementos, devolverlos
    print(f"Devolviendo {len(items)} resultados para la dirección: {direccion}")
    return items

@router.get("/station/search/poblacion/{poblacion}", response_model=List[Station])
def search_poblacion(poblacion: str):
    print(f"Recibiendo búsqueda por población: {poblacion}")

    # Buscar las estaciones que coincidan con la población
    items = search_by_poblacion(file_path, poblacion)
    print(f"Items encontrados: {len(items)}")

    # Si no hay coincidencias, lanzar un error
    if not items:
        print(f"No se encontraron resultados para la población: {poblacion}")
        raise HTTPException(status_code=404, detail="No se encontraron resultados para la población proporcionada")

    print(f"Devolviendo {len(items)} resultados para la población: {poblacion}")
    return items


