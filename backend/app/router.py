import time
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas
from app.respuestas import buscar_respuesta

router = APIRouter()


@router.post(
    "/consulta",
    response_model=schemas.ConsultaResponse,
    summary="Realizar una consulta legal a Leya",
)
def realizar_consulta(request: schemas.ConsultaRequest, db: Session = Depends(get_db)):
    inicio  = time.time()
    entrada = buscar_respuesta(request.pregunta)

    db_consulta = crud.crear_consulta(
        db=db,
        pregunta=request.pregunta,
        respuesta=entrada.respuesta,
        categoria=entrada.categoria,
        session_id=request.session_id,
    )

    return schemas.ConsultaResponse(
        id=db_consulta.id,
        respuesta=entrada.respuesta,
        categoria=entrada.categoria,
        fuentes=[schemas.FuenteNormativa(**f) for f in entrada.fuentes],
        tiempo_ms=int((time.time() - inicio) * 1000),
    )


@router.get(
    "/historial/{session_id}",
    response_model=list[schemas.ConsultaHistorial],
    summary="Obtener el historial de consultas de una sesión",
)
def obtener_historial(session_id: str, limit: int = 20, db: Session = Depends(get_db)):
    if limit < 1 or limit > 100:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="El parámetro limit debe estar entre 1 y 100.",
        )
    return crud.obtener_historial(db=db, session_id=session_id, limit=limit)


@router.post(
    "/valoracion",
    response_model=schemas.ValoracionResponse,
    summary="Valorar la utilidad de una respuesta de Leya",
)
def valorar_respuesta(request: schemas.ValoracionRequest, db: Session = Depends(get_db)):
    consulta = crud.registrar_valoracion(db=db, consulta_id=request.consulta_id, util=request.util)
    if not consulta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontró la consulta con id {request.consulta_id}.",
        )
    return schemas.ValoracionResponse(mensaje="Valoración registrada correctamente. ¡Gracias por tu retroalimentación!")


@router.get("/categorias", summary="Listar las categorías jurídicas disponibles")
def listar_categorias():
    return {
        "categorias": [
            {"id": "despido_indemnizacion", "nombre": "Despido e indemnizaciones"},
            {"id": "salario_minimo",        "nombre": "Salario mínimo"},
            {"id": "jornada_laboral",       "nombre": "Jornada laboral y horas extras"},
            {"id": "cesantias",             "nombre": "Cesantías"},
            {"id": "vacaciones",            "nombre": "Vacaciones"},
            {"id": "acoso_laboral",         "nombre": "Acoso laboral"},
            {"id": "prima_servicios",       "nombre": "Prima de servicios"},
            {"id": "contrato_trabajo",      "nombre": "Tipos de contrato"},
        ]
    }


@router.get("/health", summary="Verificar el estado del servicio")
def health_check():
    return {"status": "ok", "servicio": "Leya API", "version": "1.0.0"}
