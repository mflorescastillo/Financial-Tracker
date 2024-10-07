# backend/Dockerfile
FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install Flask Flask-CORS psycopg2-binary Flask-SQLAlchemy

CMD ["python", "app.py"]
