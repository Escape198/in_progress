FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /new

COPY . .

RUN chmod -R 777 ./

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
