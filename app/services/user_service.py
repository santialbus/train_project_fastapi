from sqlalchemy.orm import Session
from app.models.user import User
from app.services.auth.auth_service import hash_password, verify_password
from app.schemas.user import UserCreate, UserResponse
from datetime import datetime

def create_user(db: Session, user_data: UserCreate) -> UserResponse:
    """Registra un nuevo usuario con contraseña encriptada."""
    
    # Hashear la contraseña
    hashed_password = hash_password(user_data.password)
    
    # Crear el nuevo usuario
    db_user = User(
        nombre=user_data.nombre,
        email=user_data.email,
        username=user_data.username,
        telefono=user_data.telefono,
        fecha_nacimiento=user_data.fecha_nacimiento,
        activo=user_data.activo,
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return UserResponse(
        id=db_user.id,
        nombre=db_user.nombre,
        email=db_user.email,
        username=db_user.username,
        telefono=db_user.telefono,
        fecha_nacimiento=db_user.fecha_nacimiento,
        activo=db_user.activo,
        fecha_registro=db_user.fecha_registro
    )

def get_user_by_id(db: Session, user_id: int) -> UserResponse | None:
    """Obtiene un usuario por ID."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        return UserResponse(
            id=db_user.id,
            nombre=db_user.nombre,
            email=db_user.email,
            username=db_user.username,
            telefono=db_user.telefono,
            fecha_nacimiento=db_user.fecha_nacimiento,
            activo=db_user.activo,
            fecha_registro=db_user.fecha_registro
        )
    return None

def authenticate_user(db: Session, username: str, password: str) -> User | None:
    """Autentica un usuario verificando su contraseña."""
    
    db_user = db.query(User).filter(User.username == username).first()
    if db_user and verify_password(password, db_user.hashed_password):
        return db_user
    return None
