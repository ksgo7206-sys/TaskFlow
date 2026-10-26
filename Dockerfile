
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY my-docker-app/app.py .
COPY my-docker-app/templates/ templates/
COPY my-docker-app/templates/static/ static/

EXPOSE 5000

CMD ["python", "app.py"]
