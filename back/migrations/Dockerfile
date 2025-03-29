FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY migrations/ /app/migrations/
COPY alembic.ini /app/alembic.ini
COPY db/ /app/db/
COPY .env /app/.env
COPY settings.py /app/settings.py

CMD ["alembic", "upgrade", "head"]