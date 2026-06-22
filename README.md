# Backend Promotick

Backend desarrollado con **FastAPI** para la gestión, procesamiento y análisis de tickets operativos.

El proyecto permite cargar archivos CSV de tickets, realizar un proceso de limpieza y transformación de datos, almacenar la información procesada y exponer diferentes endpoints para obtener métricas operativas.

---

# Tecnologías utilizadas

- Python 3.13
- FastAPI
- Uvicorn
- Pandas
- NumPy
- SciPy
- SQLite
- Docker

---

# Estructura del proyecto

Backend_Promotick/
│
├── models/
│   └── Modelos Pydantic para validación de datos
│
├── routes/
│   ├── auth.py
│   ├── upload.py
│   └── metrics.py
│
├── services/
│   ├── storage_service.py
│   ├── cleaning_service.py
│   └── metrics_service.py
│
├── uploads/
│   └── Archivos CSV originales cargados
│
├── processed/
│   └── Archivos CSV procesados y limpios
│
├── app.db
│   └── Base de datos SQLite
│
├── Dockerfile
│
├── docker-compose.yml
│
├── requirements.txt
│
└── main.py
