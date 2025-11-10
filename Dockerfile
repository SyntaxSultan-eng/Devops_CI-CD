FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt
#-user - в домашнюю папку пользователя вместо системной
#--no-cache-dir - не сохраняем кэш установки 

###################################################

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
#Здесь лежат все установленные пакеты Python

ENV PATH=/root/.local/bin:$PATH 
#для того чтобы pip install или что-то другое можно было использовать из разных папок

COPY . .

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["python", "myproject/manage.py", "runserver", "0.0.0.0:8000"]