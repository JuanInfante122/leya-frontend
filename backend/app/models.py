from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func
from app.database import Base


class Consulta(Base):
    __tablename__ = "consultas"

    id             = Column(Integer, primary_key=True, index=True)
    session_id     = Column(String(64), index=True, nullable=False)
    pregunta       = Column(Text, nullable=False)
    respuesta      = Column(Text, nullable=False)
    categoria      = Column(String(50), nullable=True)
    util           = Column(Boolean, nullable=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())


class Usuario(Base):
    __tablename__ = "usuarios"

    id              = Column(Integer, primary_key=True, index=True)
    nombre          = Column(String(100), nullable=False)
    email           = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    activo          = Column(Boolean, default=True)
    fecha_registro  = Column(DateTime(timezone=True), server_default=func.now())
