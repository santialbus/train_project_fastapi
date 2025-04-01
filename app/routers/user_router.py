from fastapi import APIRouter, HTTPException, Depends, Form, status
from app.schemas.user import UserCreate, UserResponse, LoginCredentials
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
    credentials: LoginCredentials,  # Use the Pydantic model
    db: Session = Depends(get_db)
):
    user = user_service.authenticate_user(db=db, username=credentials.username, password=credentials.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = auth_service.create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=30)
    )

    return {"access_token": access_token, "token_type": "bearer"}

from fastapi import Response

@router.options("/users/login")
async def options_login(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

