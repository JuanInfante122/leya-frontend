from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime


class ConsultaRequest(BaseModel):
    pregunta:   str
    session_id: str

    @field_validator("pregunta")
    @classmethod
    def pregunta_no_vacia(cls, v):
        if not v or not v.strip():
            raise ValueError("La pregunta no puede estar vacía.")
        if len(v.strip()) < 5:
            raise ValueError("La pregunta debe tener al menos 5 caracteres.")
        if len(v) > 500:
            raise ValueError("La pregunta no puede superar los 500 caracteres.")
        return v.strip()

    @field_validator("session_id")
    @classmethod
    def session_valida(cls, v):
        if not v or not v.strip():
            raise ValueError("El session_id no puede estar vacío.")
        return v.strip()


class FuenteNormativa(BaseModel):
    norma:       str
    descripcion: str


class ConsultaResponse(BaseModel):
    id:        int
    respuesta: str
    categoria: str
    fuentes:   list[FuenteNormativa]
    tiempo_ms: int

    class Config:
        from_attributes = True


class ValoracionRequest(BaseModel):
    consulta_id: int
    util:        bool


class ValoracionResponse(BaseModel):
    mensaje: str


class ConsultaHistorial(BaseModel):
    id:             int
    pregunta:       str
    respuesta:      str
    categoria:      str
    util:           Optional[bool]
    fecha_creacion: datetime

    class Config:
        from_attributes = True


class UsuarioCreate(BaseModel):
    nombre:   str
    email:    EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def password_seguro(cls, v):
        if len(v) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        return v


class UsuarioResponse(BaseModel):
    id:     int
    nombre: str
    email:  str
    activo: bool

    class Config:
        from_attributes = True
