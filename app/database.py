from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base  # Importamos Base desde aquí
DATABASE_URL = "sqlite:///./test.db"  # Cambia la URL de la base de datos según tus necesidades

# Crea el motor y la sesión
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea todas las tablas en la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()