# Лабораторная работа №3: Разработка REST API

## Цель работы

Освоить проектирование RESTful API с валидацией данных, документацией и адаптацией под научные задачи. Интегрировать API с Docker и PostgreSQL.

## Реализованные возможности

- REST API на Flask с использованием Blueprints и версионированием (v1)
- Валидация входных данных через Marshmallow (SensorReadingSchema)
- Документация API через Swagger UI (flask-restx)
- Адаптация под научную тему: ML-прогнозирование (эндпоинт /predict)
- Обработка ошибок и логирование запросов
- Интеграция с PostgreSQL (модель SensorReading, сохранение и чтение данных)
- Запуск в Docker Compose (backend + postgres)

## Технологии

- Python 3.12
- Flask, Flask-RESTx
- Marshmallow
- SQLAlchemy, psycopg2-binary
- PostgreSQL 15
- Docker, Docker Compose

## Структура проекта
<img width="165" height="308" alt="image" src="https://github.com/user-attachments/assets/34232840-a85d-4e90-a4cd-d8cd61eb1ca1" />



## Запуск с помощью Docker Compose

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/bulochnikoff/Lab3.git
   cd Lab3

2.Запустить контейнеры:

bash
docker compose up --build

3.API будет доступно по адресу: http://localhost:5001



Эндпоинты API
Метод	        URL	                            Описание
GET	       /health	                    Проверка работоспособности
GET	       /api/v1/sensors/test	        Тестовый эндпоинт
GET	       /api/v1/sensors/readings	    Получить все показания датчиков
POST	     /api/v1/sensors/readings	    Добавить новое показание
POST	     /api/v1/models/predict	      ML-прогноз (сумма признаков)
GET	       /api/docs	                  Swagger UI документация

Примеры запросов
Добавление показания датчика (POST)
bash
curl -X POST http://localhost:5001/api/v1/sensors/readings \
  -H "Content-Type: application/json" \
  -d '{
    "sensor_id": "123456789012345678901234567890123456",
    "value": 25.5,
    "timestamp": "2026-05-09T12:00:00Z",
    "location": {"lat": 55.75, "lon": 37.61}
  }'
Ответ (201):

json
{
  "status": "success",
  "data": { ... }
}


Получение всех показаний (GET)
bash
curl http://localhost:5001/api/v1/sensors/readings
Ответ (200):

json
[
  {
    "id": 1,
    "sensor_id": "...",
    "value": 25.5,
    "timestamp": "...",
    "location": {"lat": 55.75, "lon": 37.61}
  }
]


ML-прогноз (POST)
bash
curl -X POST http://localhost:5001/api/v1/models/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1, 2, 3, 4]}'
Ответ (200):

json
{
  "prediction": 10,
  "status": "success"
}


Документация Swagger
Интерактивная документация доступна по адресу:
http://localhost:5001/api/docs
