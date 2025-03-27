from app.models.user import UserCreate, UserResponse, UserDB
from app.services.auth.auth_service import hash_password, verify_password
from datetime import datetime

# Base de datos simulada (diccionario en memoria)
FAKE_DB = {}

def create_user(user_data: UserCreate) -> UserResponse:
    """Registra un nuevo usuario con contraseña encriptada."""
    
    hashed_password = hash_password(user_data.password)  
    user_id = len(FAKE_DB) + 1  

    new_user = UserDB(
        id=user_id,
        fecha_registro=datetime.utcnow(),
        hashed_password=hashed_password,
        **user_data.dict(exclude={"password"})  # Excluye la contraseña en texto plano
    )

    FAKE_DB[user_id] = new_user  # Guarda el usuario en la "DB"
    
    return UserResponse(**new_user.dict())

def get_user_by_id(user_id: int) -> UserResponse | None:
    """Obtiene un usuario por ID."""
    user = FAKE_DB.get(user_id)
    return UserResponse(**user.dict()) if user else None

def authenticate_user(username: str, password: str) -> UserDB | None:
    """Autentica un usuario verificando su contraseña."""
    
    for user in FAKE_DB.values():
        if user.username == username and verify_password(password, user.hashed_password):
            return user  # Usuario autenticado
    
    return None  # Credenciales incorrectas
