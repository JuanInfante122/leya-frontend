# Leya Backend

API REST con FastAPI + SQLite para el asistente legal Leya.

## Stack

- FastAPI + Uvicorn
- SQLAlchemy + SQLite
- Pydantic v2

## Instalación local

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/api/v1/consulta` | Consulta legal al asistente |
| GET | `/api/v1/historial/{session_id}` | Historial de una sesión |
| POST | `/api/v1/valoracion` | Valorar una respuesta |
| GET | `/api/v1/categorias` | Categorías jurídicas disponibles |
| GET | `/api/v1/health` | Estado del servicio |

Documentación interactiva: `http://localhost:8000/docs`

## Despliegue en Railway

1. Conectar el repositorio en railway.app
2. Configurar Root Directory: `backend`
3. Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Variables de entorno: `DATABASE_URL`, `FRONTEND_URL`
