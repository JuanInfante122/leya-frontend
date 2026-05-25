from sqlalchemy.orm import Session
from app import models, schemas


def crear_consulta(db: Session, pregunta: str, respuesta: str, categoria: str, session_id: str) -> models.Consulta:
    db_consulta = models.Consulta(
        session_id=session_id,
        pregunta=pregunta,
        respuesta=respuesta,
        categoria=categoria,
    )
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta


def obtener_historial(db: Session, session_id: str, limit: int = 20) -> list[models.Consulta]:
    return (
        db.query(models.Consulta)
        .filter(models.Consulta.session_id == session_id)
        .order_by(models.Consulta.fecha_creacion.desc())
        .limit(limit)
        .all()
    )


def registrar_valoracion(db: Session, consulta_id: int, util: bool) -> models.Consulta | None:
    consulta = db.query(models.Consulta).filter(models.Consulta.id == consulta_id).first()
    if consulta:
        consulta.util = util
        db.commit()
        db.refresh(consulta)
    return consulta


def crear_usuario(db: Session, usuario: schemas.UsuarioCreate, hashed_password: str) -> models.Usuario:
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        hashed_password=hashed_password,
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def obtener_usuario_por_email(db: Session, email: str) -> models.Usuario | None:
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()
