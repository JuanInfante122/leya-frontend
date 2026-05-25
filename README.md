# Leya Frontend

Asistente virtual de orientación legal laboral para ciudadanos colombianos.

## Stack

- React 18 + Vite
- React Router v6
- Axios
- Context API

## Requisitos

- Node.js >= 18.x
- npm >= 9.x
- Backend Leya (FastAPI) corriendo en `http://localhost:8000/api/v1`

## Instalación

```bash
npm install
cp .env.example .env.local
# Editar .env.local con la URL del backend
```

## Comandos

```bash
npm run dev      # Desarrollo en http://localhost:5173
npm run build    # Build de producción en /dist
npm run preview  # Previsualizar el build localmente
npm run lint     # Verificar código
```

## Variables de entorno

| Variable | Descripción |
|---|---|
| `VITE_API_URL` | URL base del backend (ej: `http://localhost:8000/api/v1`) |

## Rutas

| Ruta | Descripción | Auth |
|---|---|---|
| `/` | Landing page | No |
| `/login` | Inicio de sesión | No |
| `/chat` | Chat con Leya | No |
| `/historial` | Historial de consultas | Sí |
| `/perfil` | Datos del usuario | Sí |

## Despliegue

El proyecto está configurado para Vercel. El archivo `vercel.json` maneja las redirecciones para que React Router funcione en producción.

Configurar la variable `VITE_API_URL` en el panel de Vercel con la URL del backend de producción.
