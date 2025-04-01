from fastapi import FastAPI
from app.routers.data_router import router as data_router
from app.routers.user_router import router as user_router
from app.routers.favorite_station_router import router as favorite_station_router
from app.database import init_db  # Asegúrate de importar la función init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",  # Permite el acceso local
    "http://127.0.0.1",
    "http://10.0.2.2",
    "http://192.168.18.86",  # Añadir la IP de tu máquina
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (including OPTIONS)
    allow_headers=["*"],  # Allow all headers
)

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
