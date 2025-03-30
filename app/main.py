from fastapi import FastAPI
from app.routers.data_router import router as data_router
from app.routers.user_router import router as user_router
from app.routers.favorite_station_router import router as favorite_station_router
from app.database import init_db  # Asegúrate de importar la función init_db

app = FastAPI()

# Incluyendo los routers
app.include_router(data_router)
app.include_router(user_router)
app.include_router(favorite_station_router)

# Inicialización de la base de datos al arrancar la aplicación
@app.on_event("startup")
async def startup_event():
    # Inicializa la base de datos
    init_db()
    
    # Imprime las rutas registradas
    print("Rutas registradas:")
    for route in app.routes:
        print(route.path)

print("El servidor está funcionando correctamente.")  
