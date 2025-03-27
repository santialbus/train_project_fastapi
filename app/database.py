from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import Base

DATABASE_URL = "sqlite:///./test.db"  # Cambia la URL de la base de datos según tus necesidades

# Crea el motor y la sesión
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)
