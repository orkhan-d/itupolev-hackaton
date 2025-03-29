FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY api/ /app/api/
COPY db/ /app/db/
COPY .env /app/.env
COPY settings.py /app/settings.py

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0"]