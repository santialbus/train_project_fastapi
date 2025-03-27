from fastapi import FastAPI
from app.routers.data_router import router as data_router
from app.routers.user_router import router as user_router


app = FastAPI()

app.include_router(data_router)
app.include_router(user_router)

@app.on_event("startup")
async def startup_event():
    print("Rutas registradas:")
    for route in app.routes:
        print(route.path)

print("El servidor está funcionando correctamente.")  

