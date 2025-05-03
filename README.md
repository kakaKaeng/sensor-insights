# Sensor Insights

---

## Quick Started

### 1.Setup Env file

create `.env` file

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=Dummy
POSTGRES_DB=sensor_insights_db

# Backend
DJANGO_SETTINGS_MODULE=config.settings.local
DEBUG=True
DATABASE_USER=postgres
DATABASE_PASSWORD=Dummy
DATABASE_NAME=sensor_insights_db
DATABASE_HOST=postgres
DATABASE_PORT=5432
SECRET_KEY=Dummy
X_API_KEY=Dummy

# Frontend
VITE_API_HOST=http://127.0.0.1:8000/
VITE_API_KEY=Dummy
```

### 2.Run with Docker Compose

```bash
docker compose up -d

// first time
docker compose exec backend sh -c 'uv run manage.py migrate'

// create super user (for import csv in django admin)
docker compose exec backend sh -c 'uv run manage.py createsuperuser'
```

open http://localhost:8080/

### 3.Run mock ingest data (Optional)

```bash
cd tools
python mock_ingest_data.py Dummy
```
