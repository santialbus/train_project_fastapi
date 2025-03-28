from fastapi import APIRouter, HTTPException, Depends, Form
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service
from app.services.auth import auth_service
from datetime import timedelta
from sqlalchemy.orm import Session
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = user_service.create_user(db=db, user_data=user)
        return UserResponse.from_orm(new_user)
    except HTTPException as e:
        raise e 
    
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/users/login")
def login_user(
    username: str = Form(...), 
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = user_service.authenticate_user(db=db, username=username, password=password)
    
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    access_token = auth_service.create_access_token(
        data={"sub": user.username}, 
        expires_delta=timedelta(minutes=30)
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
