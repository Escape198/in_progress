FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

COPY new .

RUN chmod -R 777 ./

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
