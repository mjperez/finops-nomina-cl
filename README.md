# FinOps & Nómina CL

Micro-SaaS B2B Fullstack para automatización de remuneraciones en Chile, validación y exportación de archivos Previred (estándar de 105 campos), conciliación transaccional con Transbank Webpay Plus REST y auditoría previsional asistida por IA con anonimización de datos personales.

## Stack Tecnológico

- **Backend:** Python 3.12, FastAPI, SQLAlchemy, Pydantic, Pytest, Ruff
- **Frontend:** React, TypeScript, Tailwind CSS, Vite
- **Base de Datos:** PostgreSQL 16
- **Infraestructura y CI:** Docker Compose, GitHub Actions

## Ejecución Local con Docker

```bash
docker compose up --build
```

- **Backend Healthcheck:** [http://localhost:8000/health](http://localhost:8000/health)
- **Documentación OpenAPI (Swagger):** [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
- **Frontend Web:** [http://localhost:5173](http://localhost:5173)

## Ejecución de Pruebas (Backend)

```bash
pytest backend
```
