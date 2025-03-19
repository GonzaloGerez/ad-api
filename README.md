# ad-api

## Descripción

Este proyecto es una API desarrollada con FastAPI que utiliza SQLAlchemy para la gestión de la base de datos, Pydantic para la validación de datos, Alembic para las migraciones y Pytest para las pruebas.

## Requisitos

- Python 3.8 o superior
- PostgreSQL u otro sistema de gestión de bases de datos compatible
- Entorno virtual de Python (recomendado)

## Configuración del entorno

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/GonzaloGerez/ad-api.git
   cd ad-api
   ```

2. **Crear y activar un entorno virtual:**

   En sistemas Unix/macOS:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

   En Windows:

   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno:**

   Renombrar el archivo `.env.example` a `.env` y completar las variables necesarias:

   ```bash
   cp .env.example .env
   ```

   ### Archivo `.env.example`:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
   ```

## Migraciones con Alembic

1. **Inicializar Alembic (si es la primera vez):**
   ```bash
   alembic init alembic
   ```

2. **Generar una nueva migración:**
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

3. **Aplicar las migraciones a la base de datos:**
   ```bash
   alembic upgrade head
   ```

## Ejecutar el servidor

Para iniciar el servidor FastAPI en modo desarrollo:

```bash
uvicorn app.main:app --reload
```

Accede a la documentación interactiva en:

- [OpenAPI Docs](http://127.0.0.1:8000/doc#)

## Pruebas con Pytest

Ejecutar los tests con:

```bash
pytest
```

Para ver detalles de cada prueba:
```bash
pytest -v
```
