from fastapi import APIRouter, HTTPException, Depends, Form
from app.models.user import UserCreate, UserResponse
from app.services import user_service
from app.services.auth import auth_service
from datetime import timedelta

router = APIRouter()

# **1️⃣ Endpoint para registrar usuario**
@router.post("/users/register", response_model=UserResponse)
def register_user(user: UserCreate):
    return user_service.create_user(user)

# **2️⃣ Endpoint para obtener usuario por ID**
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# **3️⃣ Endpoint para autenticar y generar token**
@router.post("/users/login")
def login_user(
    username: str = Form(...), 
    password: str = Form(...)
):
    user = user_service.authenticate_user(username, password)
    
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    access_token = auth_service.create_access_token(
        data={"sub": user.username}, 
        expires_delta=timedelta(minutes=30)
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
