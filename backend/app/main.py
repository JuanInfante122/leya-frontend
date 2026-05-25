from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

from app.database import Base, engine
from app.router import router

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=os.getenv("APP_NAME", "Leya API"),
    version=os.getenv("APP_VERSION", "1.0.0"),
    description=(
        "API REST del asistente virtual de orientación legal Leya. "
        "Especializada en derecho laboral colombiano. "
        "Las respuestas son orientativas y no reemplazan la asesoría de un abogado."
    ),
    contact={
        "name": "Juan Manuel Infante Quiroga",
        "url": "https://github.com/JuanInfante122/leya-frontend",
    },
    license_info={"name": "MIT"},
)

FRONTEND_URL = os.getenv("FRONTEND_URL", "https://leya-frontend.vercel.app")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        FRONTEND_URL,
        "http://localhost:5173",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor. Por favor intente nuevamente."},
    )


app.include_router(router, prefix="/api/v1", tags=["Leya"])


@app.get("/", include_in_schema=False)
def root():
    return {"mensaje": "Bienvenido a Leya API v1.0", "docs": "/docs", "estado": "operativo"}
